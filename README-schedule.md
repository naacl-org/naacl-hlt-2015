
## Pre-processing

Generate the schedule in the `Schedule Maker` tab and then download
the `accepted.zip` file using the `Download an archive` option.
Unzip it into this directory: `softconf/accepted-papers`.

Do the same for the demonstrations and unzip it into
the directory: `softconf/accepted-demos`.

Delete all the PDF files if any were part of the zip files.

Put the `order` file that was created by the Softconf schedule
maker into the `softconf` directory.

## Generating the YAML data

The Python 3 script `generate_schedule_data.py` reads the `softconf`
directory and generates a database in YAML format. This database
should be put in the file `_data/schedule.yaml`, like this:

    python3 generate_schedule_data.py > _data/schedule.yaml

