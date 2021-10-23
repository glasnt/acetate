from pathlib import Path

import pytest
from bs4 import BeautifulSoup as bs
from cli import pager
from click.testing import CliRunner

GOOGLE_SAMPLES = "samples/google-slides/"
POWERPOINT_SAMPLES = "samples/microsoft-365-powerpoint/"

SLIDES_FN = "sample-notes.pdf"
NOTES_FN = "sample-notes.pdf"


def test_google_slides():
    runner = CliRunner()
    result = runner.invoke(
        pager, ["-s", GOOGLE_SAMPLES + SLIDES_FN, "-n", GOOGLE_SAMPLES + NOTES_FN]
    )
    assert result.exit_code == 0
    assert Path("generated_sample-slides").exists()

    with open("generated_sample-slides/slides.html") as f:
        html = bs(f.read(), "html.parser")

    assert "Sample Presentation" in html.title.text
    assert "Here is a picture of my dog" in html.body.text


@pytest.mark.skip
def test_microsoft_365():
    runner = CliRunner()
    result = runner.invoke(
        pager,
        ["-s", POWERPOINT_SAMPLES + SLIDES_FN, "-n", POWERPOINT_SAMPLES + NOTES_FN],
    )
    assert result.exit_code == 0
    assert Path("generated_sample-slides").exists()

    with open("generated_sample-slides/slides.html") as f:
        html = bs(f.read(), "html.parser")

    assert "Sample Presentation" in html.title.text
    assert "Here is a picture of my cat" in html.body.text
