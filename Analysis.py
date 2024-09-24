import fitz  # PyMuPDF
from transformers import BertForQuestionAnswering, BertTokenizer
import torch


def read_pdf_text(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""

    # Iterate over each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)  # Load the page
        text += page.get_text()  # Extract text from the page

    return text

# Example usage:
pdf_path = 'Paper 1.pdf'  # Replace with your PDF file path
context = read_pdf_text(pdf_path)

# Define the question
question = "Does Ba3Cu14.35Se8.55Te2.45 need to be hotpressed?"
print(context)