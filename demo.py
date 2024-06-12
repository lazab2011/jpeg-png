# Floyd Brooks
# June 2024
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










