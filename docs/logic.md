
## Logic Discussion

### Handling overflow

In cases where notes overflow on to a second page, there needs to be a staggered offset of content. 

Some possible algorithms to check if this happens 

 * If the slide text does not appear in the notes text
    * see "Edge case": Left content"
 * If the slide text is longer in length than the notes text
    * edge case: if there is an overflow of text is less than the amount of text on the slide

The current algorithm is to assume an overflow if a rectangle shape does not appear on a notes page. *This presumes a format where the slides on a notes page has a rectangle outline.* A lack of rectangle indicates an overflow. 

### Removing slide content

In most cases, the text of a slide can be completely removed from a text of a notes page. 

#### Edge case: left content

However, in cases were text appears on a slide on the utmost left hand side of the page, this can make the text extraction process differ between slide and notes. (The assumption here being because of the placement of the slide on the notes render is inset, there can be instances where the text is read differently.)

In these cases, it's up to the user to remove the text.

## Edge case: Powerpoint title

In the case of Powerpoint, the name of the PDF file is titleized into the title of the PDF, as opposed to the name of the slides in Powerpoint. 