from pathlib import Path
import sys
import pdfplumber
import yaml
from bs4 import BeautifulSoup as bs


IMAGES_DIR = "images"
YAML_FILE = "slides.yaml"
HTML_FILE = "index.html"

from .utils import cleanup_text


def generate_data(slides, notes, output):
    """From two files, process into a folder of data"""
    results_file = f"{output}/{YAML_FILE}"
    Path(output).mkdir(exist_ok=True)
    Path(output).joinpath(IMAGES_DIR).mkdir(exist_ok=True)

    slides_yaml = []
    results_yaml = {}

    with pdfplumber.open(slides) as pdf:
        if "Title" in pdf.metadata:
            title = pdf.metadata["Title"]
        else:
            title = Path(slides.name).stem.title()
        results_yaml["title"] = title
        slide_pages = pdf.pages

    with pdfplumber.open(notes) as pdf:
        notes_pages = pdf.pages

    notes_offset = 0
    for n in range(0, len(slide_pages)):
        sys.stderr.write(
            f"\r{n}/{len(slide_pages)} ({round(n/len(slide_pages) * 100)}%)"
        )
        sys.stderr.flush()

        slide = slide_pages[n]
        notes = notes_pages[n + notes_offset]

        notes_text = notes.extract_text()
        slides_text = slide.extract_text()

        # If the notes page doesn't have a box on it, it's overflow
        # TODO only handles one overflow.
        # TODO investigate tolerance (gs has rects, pp doesn't)
        if not any([x["linewidth"] for x in notes.rects]):
            # print(f"Slide {n} doesn't match notes {n + notes_offset}")
            slides_yaml[-1]["text"] += notes_text
            notes_offset += 1
            notes_text = notes.extract_text()
            notes = notes_pages[n + notes_offset]

        text = notes_text.replace(slides_text or "", "", 1).strip()
        text = cleanup_text(text)
        image_fn = Path(IMAGES_DIR).joinpath(f"slide_{n}.png")
        slide.to_image(resolution=150).save(
            str(Path(output).joinpath(image_fn)), format="PNG"
        )
        slides_yaml.append({"image": str(image_fn), "alt": slides_text, "text": text})

    results_yaml["slides"] = slides_yaml

    with open(results_file, "w") as f:
        yaml.dump(results_yaml, f)

    print(f"\n\nYAML data saved to {results_file}")


def generate_html(data_dir, css):
    """Given a datafile of generated data, make some pretty HTML
    Not necessarily the complete end result, but a useful preview of the data"""
    with open(Path(data_dir).joinpath(YAML_FILE)) as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)

    styling = css.read().decode("UTF-8")

    title = data.get("title", "Generated Slides")
    html = [
        f"""<!DOCTYPE html>
    <html lang="en">
    <title>{title}</title>
    <style>{styling}</style>
    <body>
    <h1>{title}</h1>
    <div class='container'>
    """
    ]

    for slide in data["slides"]:
        html.append(
            f"""<div class='row'>
            <div class='slide'><img alt='{slide['alt']}' src='{slide['image']}' /></div>
            <div class='notes'>{slide['text']}</div>
            </div>
            """
        )
    html.append("</div></body></html>")
    html = "\n".join(html)
    root = bs(html, "html.parser")
    prettyHTML = root.prettify()

    with open(Path(data_dir).joinpath(HTML_FILE), "w") as f:
        f.write(prettyHTML)

    print(f"HTML data saved to {data_dir}")
