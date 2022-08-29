
# Read Multiple PDFs From One Folder And Write To Text Files In Another Folder

# PyPDF2

from PyPDF2 import PdfFileReader
from pathlib import Path
import glob

for pdfFile in Path("pdfs").glob("*.pdf"):

# Create pdf file reader object

    pdf = PdfFileReader(pdfFile)

# Grab the page(s)

    page_1_object = pdf.getPage(0)

# Extract text

    page_1_text = page_1_object.extractText()


# Combine the text from all the pages and save as txt file

    with open("txts/{}.txt".format(pdfFile.stem), mode='w', encoding="utf-8") as file:
        for page in pdf.pages:
            text = ''
            text += page.extractText()
            file.write(text)
            file.close