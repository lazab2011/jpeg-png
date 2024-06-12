# import PyPDF2
# import sys
# import os

from PyPDF2 import PdfFileMerger
from PyPDF2.errors import PdfReadError

## Counting pages
# with open("twopage.pdf", "rb") as f:
#     reader = PyPDF2.PdfReader(f)
#     num_pages = len(reader.pages)
#     print(num_pages)

# read page 1
# with open("dummy.pdf", "rb") as f:
#     reader = PyPDF2.PdfReader(f)
#     page = reader.pages[0]
#     get_text = page.extract_text()
#     print(get_text)


# rotate a pdf document

# with open("dummy.pdf", "rb") as f:
#     reader = PyPDF2.PdfReader(f)
#     page = reader.pages[0]
#     page.rotate(-270)
#
#     # write the file
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#     with open("new_dummy.pdf", "wb") as f:
#         writer.write(f)


# merge PDF

# input_pdf = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     file_merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         try:
#             file_merger.append(pdf)
#         except FileNotFoundError:
#             print("file,{pdf}, not found")
#         except PdfReadError:
#             print("I am sorry, but you do not have the required pdf file")
#         except PyPDF2.errors as e:
#             print(f"I am sorry, but you do not have the required pdf file {e}")
#
#             file_merger.write("Merged.pdf")
#
# pdf_combiner(input_pdf)

import PyPDF2
import sys
import os


def pdf_combiner(in_path, des_path):
    docs = []
    merger = PyPDF2.PdfWriter()
    for file in os.listdir(in_path):
        if file.endswith(".pdf"):
            docs.append(file)
    for doc in docs:
        with open(doc, "rb") as pdf_file:
            merger.append(pdf_file)

# Ensure that the destination directory exists
    if not os.path.exists(des_path):
        os.mkdir(des_path)

# write the merged PDF to the destination path
    merged_pdf_path = os.path.join(des_path, "Merged_pdf.pdf")
    with open(merged_pdf_path, "wb") as merged_pdf_file:
        merger.write(merged_pdf_file)

# Define paths
in_path = os.path.join(r"C:\Users\dyolf\OneDrive\Desktop\demo")
des_path = os.path.join(r"C:\Users\dyolf\OneDrive\Desktop\demo")

# combine pdfs
merged = pdf_combiner(in_path, des_path)










