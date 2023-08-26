from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="acetate",
    description="Convert slide PDFs into readable HTML",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Katie McLaughlin",
    url="https://github.com/glasnt/acetate",
    project_urls={
        "Issues": "https://github.com/glasnt/acetate/issues",
        "CI": "https://github.com/glasnt/acetate/actions",
        "Changelog": "https://github.com/glasnt/acetate/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["acetate"],
    entry_points="""
        [console_scripts]
        acetate=acetate.cli:cli
    """,
    install_requires=[
        "click",
        "pdfplumber",
        "pillow",
        "pyyaml",
        "beautifulsoup4",
    ],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.11",
)
