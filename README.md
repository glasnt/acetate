# Acetate

![Acetate logo](docs/acetate.png)

*This code base is considered exceptionally alpha. It will break, and you get to keep the shiny pieces.*

Take two PDFs -- one with slides, and one with slides and speaker notes -- and generate one HTML.

Make for a nice format for reading slides in a webpage, allowing for richer interactions etc for people who learn better that way. 

This is currently used in the writeups on [glasnt.com/talks](https://glasnt.com/talks).

## Invocation

```
$ acetate --help
Usage: acetate [OPTIONS]

Options:
  -s, --slides FILENAME  PDF of slides
  -n, --notes FILENAME   PDF of slides with speaker notes
  -o, --output TEXT      Output folder
  -c, --css FILENAME     Optional styling file
  --help                 Show this message and exit.
```

Example from testing data: 

```
$ acetate \
    -s samples/google-slides/sample-slides.pdf \
    -n samples/google-slides/sample-notes.pdf
```

## Outputs

```
$ tree generated
generated
├── images
│   ├── slide_0.png
│   ├── slide_1.png
│   ├── slide_2.png
│   └── slide_3.png
├── index.html
└── slides.yaml

2 directories, 6 files
```

You can customise the HTML output, or use the `slides.yaml`` directly in things like static site generators. 

---

Read more about: [Concept](docs/concept.md), [how to export slides](docs/howto.md), [logic decisions](docs/logic.md)


## Licence

See LICENCE

Logo CC-BY-3.0 Kristin Poncek Jones, the Noun Project