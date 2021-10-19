from pathlib import Path

import click
import pdfplumber
import yaml

IMAGES = 'images'

def generate_data(slides, notes):
    """From two files, process into a folder of data"""
    results_dir = f"generated_{Path(slides.name).stem}"
    results_file = f"{results_dir}/slides.yaml"
    Path(results_dir).mkdir(exist_ok=True)
    Path(results_dir).joinpath(IMAGES).mkdir(exist_ok=True)

    results_yaml = []

    with pdfplumber.open(slides) as pdf:
        slide_pages = pdf.pages
    
    with pdfplumber.open(notes) as pdf:
        notes_pages = pdf.pages

    notes_offset = 0
    for n in range(0, len(slide_pages)):
        slide = slide_pages[n]
        notes = notes_pages[n + notes_offset]

        notes_text = notes.extract_text()
        slides_text = slide.extract_text()

        # Handle case where notes extend past one page
        # TODO handle cases where, for some reason, the extract_text changes the slide-render between exports
        # (eg deployment talk slide 55/notes 56)
        if slides_text not in notes_text:
            print(f"Slide {n} doesn't match notes {n + notes_offset}")
            results_yaml[-1]["text"] += notes_text
            breakpoint()
            notes_offset += 1
            notes_text = notes.extract_text()
            notes = notes_pages[n + notes_offset]

        text = notes.extract_text().replace(slide.extract_text(), "").strip()
        image_fn = Path(IMAGES).joinpath(f"slide_{n}.png")
        slide.to_image().save(str(Path(results_dir).joinpath(image_fn)), format="PNG")
        results_yaml.append( {"image": str(image_fn), "text": text })

    with open(results_file, "w") as f:
        yaml.dump(results_yaml, f)
    
    return results_dir

def generate_html(data_dir):
    """Given a datafile of generated data, make some pretty HTML"""
    with open(Path(data_dir).joinpath("slides.yaml")) as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    
    html = ["""<html>
    <style>
    img { width: 200px; border: 1px solid black;}
    .notes { width: 300px; font: sans; }
    </style>
    <table>"""]

    for slide in data:
        html.append(f"<tr><td><img src='{slide['image']}' /></td><td class='notes'>{slide['text']}</td></tr>")
    
    with open(Path(data_dir).joinpath("slides.html"), 'w') as f:
        f.write("\n".join(html))


@click.command()
@click.option('--slides', '-s', help="PDF of slides", type=click.File('rb'))
@click.option('--notes', '-n', help="PDF of slides with speaker notes", type=click.File('rb'))
def pager(slides, notes):
    data_dir = generate_data(slides, notes)
    generate_html(data_dir)



if __name__ == "__main__": 
    pager()
