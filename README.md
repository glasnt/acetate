# Slides Pager

Take two PDFs, generate one HTML.

Make for a nice format for reading slides in a webpage, allowing for richer interactions etc for people who learn better that way. 

### Concept

Take two PDFs: 
 
 * one of just your slides (used for screenshots)
 * one of your slides and speaker notes (used for text)

For each page: 
 * Screenshot all the slides and make into images. 
 * Extract the speaker notes (all the text on the page, minus the text on the same page in the slides PDF)
 
Export the images and text into a format that you can then edit later. (maybe a YAML format, then export that to HTML?) 

In theory this should handle multiple types of PDF exports, given the diff formatting. 

## Tests

```
python cli.py -s tests/sample-slides.pdf -n tests/sample-notes.pdf 
```

### How to get outputs

#### Google Slides

* Go to File > Print Settings And Preview
* Slides: 
  * In ribbon:
    * select "1 slide without notes"
    * unselect "Include skipped slides"
    * click "Download as PDF"

* Slides and Notes: 
  * In ribbon: 
    * select "1 slide with notes"
    * unselect "Include skipped slides"
    * click "Download as PDF"