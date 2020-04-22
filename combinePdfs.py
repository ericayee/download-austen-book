# goal: combine all downloaded book PDFs into a single PDF without cover pages
# heavily based on a tutorial from "Automate the Boring Stuff with Python"
# https://automatetheboringstuff.com/2e/chapter15/
import PyPDF2, os

# get all pdf file names
pdfFiles = []
files = os.listdir('book_pdfs/')

for f in files:
    pdfFiles.append(f)

# sort list of file names
sortedList = sorted(pdfFiles, key=lambda x: int("".join([i for i in x if i.isdigit()])))

# loop through all pdfs in the list and combine them
pdfWriter = PyPDF2.PdfFileWriter()
for filename in sortedList:
    pdfFileObj = open('book_pdfs/' + filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # loop through all pages except the first and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# save resulting pdf to a file
pdfOutput = open('TheMakingOfJaneAusten.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
