import shutil
from pathlib import Path

import pytest
from click.testing import CliRunner
from test_attributes import check_html_attributes

from acetate.cli import cli

SAMPLE_FOLDER = "samples"
SAMPLES = ["google-slides", "canva", "microsoft-powerpoint"]

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

    result = runner.invoke(
        cli,
        [
            "-s",
            Path(input_folder) / SLIDES_FN,
            "-n",
            Path(input_folder) / NOTES_FN,
            "-o",
            output_folder,
        ],
    )
    assert result.exit_code == 0
    assert output_folder.exists()
    assert (output_folder / "index.html").exists()

    check_html_attributes(output_folder / "index.html")
