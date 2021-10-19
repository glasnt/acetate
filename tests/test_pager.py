from pathlib import Path
from click.testing import CliRunner
from cli import pager

def test_pager():
  runner = CliRunner()
  result = runner.invoke(pager, ['-s', 'tests/sample-slides.pdf', '-n', 'tests/sample-notes.pdf'])
  assert result.exit_code == 0
  assert Path("generated_sample-slides").exists()