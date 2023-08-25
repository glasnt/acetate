from pathlib import Path

import click

from .generate import generate_data, generate_html


@click.command()
@click.version_option()
@click.option("--slides", "-s", help="PDF of just slides", type=click.File("rb"))
@click.option("--notes", "-n", help="PDF of slides with notes", type=click.File("rb"))
@click.option("--output", "-o", help="Output folder", default="generated")
@click.option(
    "--css",
    "-c",
    help="Optional styling file",
    type=click.File("rb"),
    default=Path("templates/styling.css"),
)
def cli(slides, notes, output, css):
    generate_data(slides, notes, output)
    generate_html(output, css)


if __name__ == "__main__":
    cli()
