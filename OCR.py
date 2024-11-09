from PIL import Image
import pytesseract
import numpy as np
import cv2

# Set the path to your Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the image name and construct the full file path
image_name = r"page_2.png"
filename = r"C:\Users\chris\Desktop\Nikhil\\" + image_name  # Double backslashes for path

# Open the image
img = Image.open(filename)

# Increase the size of the image (scale factor can be adjusted)
scale_factor = 10  # Change this value to increase or decrease the size
new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
img_resized = img.resize(new_size, Image.LANCZOS)  # Use LANCZOS filter for high-quality resizing

# Convert to grayscale
img_gray = img_resized.convert("L")

# Convert the image to a numpy array for OpenCV processing
img_array = np.array(img_gray)

# Perform OCR on the processed image
text = pytesseract.image_to_string(img_array)
# Print the extracted text
print(text)
