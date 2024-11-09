from PIL import Image
import pytesseract
import numpy as np

# Set the path to your Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the image name and construct the full file path
image_name = r"page_001.png"
filename = r"C:\Users\chris\Desktop\Nikhil\\" + image_name  # Double backslashes for path

# Open the image and convert it to a NumPy array
img1 = np.array(Image.open(filename))

# Perform OCR on the image
text = pytesseract.image_to_string(img1)

# Print the extracted text
print(text)