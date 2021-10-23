# Slides Pager

*This code base is considered exceptionally alpha. It will break, and you get to keep the shiny pieces.*

Take two PDFs, generate one HTML.

Make for a nice format for reading slides in a webpage, allowing for richer interactions etc for people who learn better that way. 

## Concept

Take two PDFs: 
 
 * one of just your slides (used for screenshots)
 * one of your slides and speaker notes (used for text)

For each page: 
 * Screenshot all the slides and make into images. 
 * Extract the speaker notes (all the text on the page, minus the text on the same page in the slides PDF)
 
Export the images and text into a format that you can then edit later. (maybe a YAML format, then export that to HTML?) 

In theory this should handle multiple types of PDF exports.


## Invocation

```
$ python cli.py --help
Usage: cli.py [OPTIONS]

Options:
  -s, --slides FILENAME  PDF of slides
  -n, --notes FILENAME   PDF of slides with speaker notes
  -c, --css FILENAME     Optional styling file
  --help                 Show this message and exit.
```

Example from testing data: 

```
$ python cli.py -s tests/sample-slides.pdf -n tests/sample-notes.pdf
```

## Outputs

```
generated_sample-slides
├── images 
│   ├── slide_0.png
│   ├── slide_1.png
│   └── ...
├── slides.html          # an example render
└── slides.yaml          # generated data
```

You can customise the HTML output, or use the slides.yaml directly in things like static site generators. 

## How to get slides

### Google Slides

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

### Other formats

TODO

## Logic Discussion

### Handling overflow

In cases where notes overflow on to a second page, there needs to be a stagged offset of content. 

Some possible algorithms to check if this happens 

 * If the slide text does not appear in the notes text
    * see "Edge case": Left content"
 * If the slide text is longer in length than the notes text
    * edge case: if there is an overflow of text is less than the amount of text on the slide

The current algorithm is to assume an overflow if a rectange shape does not appear on a notes page. *This presumes a format where the slides on a notes page has a rectange outline.* A lack of rectangle indicates an overflow. 

### Removing slide content

In most cases, the text of a slide can be completely removed from a text of a notes page. 

#### Edge case: left content
However, in cases were text appears on a slide on the utmost left hand side of the page, this can make the text extraction process differ between slide and notes. (The assumption here being because of the placement of the slide on the notes render is inset, there can be instances where the text is read differently.)

In these cases, it's up to the user to remove the text.

## Licence

See LICENCE
