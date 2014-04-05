# foist

PDF-redaction tools

----

`foist` is a pair of tools that make it easier to redact parts of PDF
documents. 

## History

[Froide](http://stefanw.github.io/froide/) and
[Alaveteli](http://alaveteli.org/) are plaforms for making Freedom of
Information requests in public.  Occasionally official government
responses to such requests include private information (e.g. personal
details of the person making the request), which needs to be removed from
the published document. We couldn't find any tools that allowed for
removing both textual and image-based parts, and also allowed for
keeping as much as possible of the underlying text (so as to allow
searching) — so we collaborated to make this. 

It's pretty much impossible to do a perfect job of this, but this should
work 90% of the time.

## Approach

1. Convert the PDF to HTML
  * We do this using [PDF2htmlEX](https://github.com/coolwanglu/pdf2htmlEX)
2. Provide an Edit Window 
    * Clicking on any link converts it to plain text
    * Highlighting any text replaces it with a black box
    * Selecting any part of an image replaces that part with a black box
3. Send the new 'clean' HTML back to the calling application
4. The calling application can reconvert this HTML back to a PDF, if
required. (Later versions of foist may offer this as an option.)

## Installation


## Integration 


