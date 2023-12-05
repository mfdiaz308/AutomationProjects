import PyPDF2
import os

inPath = 'PdfMerger/Input'
outPath = 'PdfMerger/Output'

merger = PyPDF2.PdfMerger()

for file in os.listdir(inPath):
    if file.endswith('.pdf'):
        merger.append(PyPDF2.PdfReader(f'{inPath}/{file}'))

out = os.path.join(outPath,'combinedPDFs.pdf')
merger.write(out)