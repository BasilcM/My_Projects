# PDF Document ID Detection
Project Breaf: Identify The Document Number from a PDF Document by the help of OCR. Dectect through NLP Search Method.


![Document Number Detection](https://github.com/BasilcM/My-Projects/blob/master/Document%20ID%20Detection/Test/Example%20Image/Document%20Number%20Detection.PNG?raw=true)

## Getting Started

This Document Detector used to detect and rename the PDF Document.

### Prerequisites

Convert pdfs, using pytesseract to do the OCR, and export each page in the pdfs to a text file.

#### Installing

```
conda install -c conda-forge pytesseract

conda install -c conda-forge tesseract

pip install pytesseract

pip install pdf2image

```
How to install [tesseract](https://guides.library.illinois.edu/c.php?g=347520&p=4121425)
---
[Tesseract GitHub Page](https://github.com/tesseract-ocr/tessdata)

##### Mac
* To install Tesseract

`brew install tesseract`

##### Windows
In Windows install [tesseract-ocr]() and also, make sure that [ Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019](https://www.visualstudio.com/downloads/) installed in your machine. A python (3.7+) module that wraps pdftoppm and pdftocairo to convert PDF to a PIL Image object
##### Linux
`pip install Tesseract`

How to install [pdf2image](https://pypi.org/project/pdf2image/)
---
`pip install pdf2image Tesseract`

##### Windows
Windows users will have to install [poppler for Windows](http://blog.alivate.com.au/poppler-windows/), then add the bin/ folder to PATH.

##### Mac
Mac users will have to install [poppler for Mac](http://macappstore.org/poppler/).

##### Linux
Most distros ship with pdftoppm and pdftocairo. If they are not installed, refer to your package manager to install poppler-utils

Platform-independant (Using conda)
Install poppler: `conda install -c conda-forge poppler`
Install pdf2image: `pip install pdf2image`
How does it work?
`from pdf2image import convert_from_path, convert_from_bytes`

##### Convert scanned pdf to text  using python

Convert Scanned/text PDF into Text.

```
import pytesseract
from pdf2image import convert_from_path
import glob

pdfs = glob.glob(r"yourPath\*.pdf")

for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 500)

    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='eng')
```

### Running the tests
---
To make sure that you have python in your system.
```
Git clone https://github.com/BasilcM/My-Projects.git
cd My-Projects/Document ID Detection/
pip install -r Anaconda requirements.txt
or
pip install -r requirements.txt

python app.py
```
Make sure that a text file and a pdf in your working file.
You can Edit the file path through the text file.

```bash
Document ID Detection
|--> app.py
|--> textfile.txt
|   ...
|-->//FilePath/#PDF files.
```
#### Author

* [Basil Chacko Mathew](https://github.com/BasilcM)

#### License

This project is licensed under the GNU License.

#### Acknowledgments
* inspiration
