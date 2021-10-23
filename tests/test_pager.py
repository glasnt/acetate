from pathlib import Path
from click.testing import CliRunner

from bs4 import BeautifulSoup as bs
from cli import pager

def test_pager():
  runner = CliRunner()
  result = runner.invoke(pager, ['-s', 'tests/sample-slides.pdf', '-n', 'tests/sample-notes.pdf'])
  assert result.exit_code == 0
  assert Path("generated_sample-slides").exists()
  
  with open("generated_sample-slides/slides.html") as f:
    html = bs(f.read(), 'html.parser')
  
  assert "Sample Presentation" in html.title.text
  assert "Here is a picture of my dog" in html.body.text
