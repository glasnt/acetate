import pdfplumber
import sys

with pdfplumber.open(sys.argv[1]) as pdf:
    test_page = pdf.pages[0]
    print(test_page.extract_text())
breakpoint()
