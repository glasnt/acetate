import shutil
from pathlib import Path

import pytest
from bs4 import BeautifulSoup as bs
from click.testing import CliRunner

from acetate.cli import cli

SAMPLE_FOLDER = "samples"
SAMPLES = ["google-slides"]  # , "microsoft-365-powerpoint", "canva"]

SLIDES_FN = "sample-slides.pdf"
NOTES_FN = "sample-notes.pdf"

GENERATED_FOLDER = "generated"


@pytest.mark.parametrize("sample_fn", SAMPLES)
def test_slides_type(sample_fn):
    runner = CliRunner()

    if Path(GENERATED_FOLDER).exists():
        shutil.rmtree(GENERATED_FOLDER)

    folder = Path(SAMPLE_FOLDER) / sample_fn

    print(f"acetate -s {Path(folder) / SLIDES_FN} -n {Path(folder) / NOTES_FN}")
    result = runner.invoke(
        cli, ["-s", Path(folder) / SLIDES_FN, "-n", Path(folder) / NOTES_FN]
    )
    assert result.exit_code == 0
    assert Path(GENERATED_FOLDER).exists()
    assert (Path(GENERATED_FOLDER) / "index.html").exists()

    with open(Path(GENERATED_FOLDER) / "index.html") as f:
        html = bs(f.read(), "html.parser")

    assert "Sample Presentation" in html.title.text
    assert "Here is a picture of my dog" in html.body.text

    shutil.move(GENERATED_FOLDER, GENERATED_FOLDER + str(folder).split("/")[-1])
