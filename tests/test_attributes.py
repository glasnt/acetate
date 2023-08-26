# Checks the attributes of the sample files

from bs4 import BeautifulSoup as bs


def check_html_attributes(html_file):
    with open(html_file) as f:
        html = bs(f.read(), "html.parser")

    # Slides file name
    assert "Sample Presentation" or "Sample-Slides" in html.title.text

    slides = html.body.findAll("div", {"class", "row"})

    # Helpers
    def notes(slide_index):
        return slides[slide_index].findAll("div", {"class": "notes"})[0].text

    def slide(slide_index):
        return slides[slide_index].img["alt"]

    # Slide one
    assert "Title Slide" in slide(0)
    assert "Jane Developer" in slide(0)
    assert "Welcome" in notes(0)

    # Slide two
    assert "Agenda" in slide(1)
    assert "Here is the agenda" in notes(1)

    # Slide three
    assert "Puppy" in slide(2)
    assert "Here is a picture of my dog" in notes(2)

    # Slide four
    assert "Thanks" in slide(3)
    assert "Thank you" in notes(3)