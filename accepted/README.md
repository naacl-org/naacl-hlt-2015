
Generate the schedule in the `Schedule Maker` tab and then download
the `accepted.zip` file using the `Download an archive` option.
Unzip it into this directory: `accepted`.  Delete all the PDF files
and then run `python remove-pdf-links.py > index.html` to generate
the index file.  Commit any changes.

The schedule needs to be integrated into the main website possibly
by generating an `index.md` file which will pick up the header and
footer HTML as well as the right CSS hopefully.
