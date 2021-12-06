# Meme Generator

A web application that generates random or custom memes.
Instructions to get you started on the meme generator project, the project will run on your local machine.

## Pre-run

Download and install the pdftotext command line tool from: https://www.xpdfreader.com/download.html
pdftotext CLI helps in accessing text information within a pdf file

## Before you begin

Install all dependencies given in the `requirements.txt` file using `pip`:
```bash
pip install -r requirements.txt
```

Application
The application can be started by running the following command:

```
python app.py
```

## Module structure

Each module has a README markdown file to explain the functionality of the module's code and its purpose in the project.

```
meme-generator - abhinav
|README.md
|app.py
|pdf_to_text.txt
|requirements.txt
|service.yml
|TODO.md
|Pipfile
|Pipfile.lock
|Dockerfile
|.travis.yml
|
|_data
   |___DogQuotes
|      |__DogQuotesCSV.csv
|      |__DogQuotesDOCX.docx
|      |__DogQuotesPDF.pdf
|      |__DogQuotesTXT.txt
|
|Fonts
|   |__Roboto-Bold.ttf
|   |__Roboto-Medium.ttf
|
|Photos
    |__Dog
|       |__xander_1.jpg
|       |__xander_2.jpg
|       |__xander_3.jpg
|       |__xander_4.jpg
|
|Simplelines
|   |__Simplelines.csv
|   |__Simplelines.docx
|   |__Simplelines.pdf
|   |__Simplelines.txt
|
|ingestors
|   |__ __init__.py
|   |__ __main__.py
|   |__ csv_ingestor.py
|   |__ docx_ingestor.py
|   |__ ingestor_interface.py
|   |__ pdf_ingestor.py
|   |__ README.md
|   |__ text_ingestor.py
|meme
|   |__ __init__.py
|   |__ __main__.py
|   |__ meme.py
|   |__ meme_engine.py
|models
|   |__ __init__.py
|   |__ quote_model.py
|   |__ README.md
|templates
|   |__ base.html
|   |__ meme.html
|   |__ meme_form.html
|   |__meme_error.html
```