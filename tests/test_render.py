import shutil
from pathlib import Path

import pytest
from bs4 import BeautifulSoup as bs
from click.testing import CliRunner

from acetate.cli import cli

SAMPLE_FOLDER = "samples"
SAMPLES = ["google-slides" , "microsoft-365-powerpoint", "canva"]

SLIDES_FN = "sample-slides.pdf"
NOTES_FN = "sample-notes.pdf"

GENERATED_FOLDER = Path("pytest_data") 


@pytest.mark.parametrize("sample_fn", SAMPLES)
def test_slides_type(sample_fn):
    runner = CliRunner()

    output_folder = GENERATED_FOLDER / sample_fn

    if Path(output_folder).exists():
        shutil.rmtree(output_folder)

    input_folder = Path(SAMPLE_FOLDER) / sample_fn

    print(f"acetate -s {Path(input_folder) / SLIDES_FN} -n {Path(input_folder) / NOTES_FN} -o {output_folder}")
    result = runner.invoke(
        cli, ["-s", Path(input_folder) / SLIDES_FN, "-n", Path(input_folder) / NOTES_FN, "-o", output_folder ]
    )
    assert result.exit_code == 0
    assert Path(GENERATED_FOLDER).exists()
    assert (Path(GENERATED_FOLDER) / "index.html").exists()

    with open(Path(GENERATED_FOLDER) / "index.html") as f:
        html = bs(f.read(), "html.parser")

    assert "Sample Presentation" in html.title.text
    assert "Here is a picture of my dog" in html.body.text

