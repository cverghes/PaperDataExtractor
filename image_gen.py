from pathlib import Path
import fitz  # PyMuPDF for PDF to image conversion
import pytesseract
from PIL import Image
import io
import platform

# Setup paths depending on the operating system
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\chris\Desktop\Nikhil\tesseract-ocr-w64-setup-5.4.0.20240606.exe"
    path_to_poppler_exe = Path(r"C:\Program Files\poppler-0.68.0\bin")
    out_directory = Path(r"~\Desktop").expanduser()
else:
    out_directory = Path("~").expanduser()

# Define PDF file path correctly
PDF_file = Path(r"Paper 1.pdf")

# Create the output folder name based on the PDF filename (without extension)
output_folder_name = PDF_file.stem  # Gets the filename without the extension
output_folder = Path(f"paper_images/{output_folder_name}")  # Create path for output folder
output_folder.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

def pdf_to_images(pdf_path, output_folder):
    """Convert PDF pages to images using PyMuPDF and save them."""
    pdf_document = fitz.open(pdf_path)
    
    # Loop through each page in the PDF and convert to image
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  # Load a single page
        pix = page.get_pixmap()  # Render page as an image
        
        # Save each page as an image
        image_filename = output_folder / f"page_{page_num + 1}.png"
        pix.save(image_filename)  # Save the image
        print(f"Saved: {image_filename}")

def main():
    pdf_to_images(PDF_file, output_folder)

if __name__ == "__main__":
    main()
