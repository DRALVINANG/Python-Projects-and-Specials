#---------------------------------------------------------------------------------------------
# Step 1: Install Required Libraries
#---------------------------------------------------------------------------------------------
!pip install pdf2image  # Install pdf2image library for PDF conversion
!apt-get install poppler-utils  # Install poppler-utils, required backend for pdf2image

#---------------------------------------------------------------------------------------------
# Step 2: Import Necessary Libraries
#---------------------------------------------------------------------------------------------
from pdf2image import convert_from_path  # Import function to convert PDF to images
from google.colab import files  # Import module to upload/download files in Colab
import os  # Import OS module to handle directory operations

#---------------------------------------------------------------------------------------------
# Step 3: Upload Your PDF File
#---------------------------------------------------------------------------------------------
uploaded = files.upload()  # Prompt user to upload their PDF file

#---------------------------------------------------------------------------------------------
# Step 4: Convert the Uploaded PDF to Images
#---------------------------------------------------------------------------------------------
pdf_file = list(uploaded.keys())[0]  # Extract the filename of the uploaded PDF

# Convert the PDF to images with high resolution (400 DPI)
images = convert_from_path(pdf_file, dpi=400)  # Set high DPI for better quality

#---------------------------------------------------------------------------------------------
# Step 5: Save the Images
#---------------------------------------------------------------------------------------------
output_dir = "/content/pdf_images"  # Directory to store output images
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

# Save each page of the PDF as a PNG image
for i, image in enumerate(images):
    image_path = f"{output_dir}/page_{i + 1}.png"  # Define output filename
    image.save(image_path, "PNG")  # Save image as PNG
    print(f"Saved {image_path}")  # Display confirmation message

#---------------------------------------------------------------------------------------------
# Step 6: Download the Images
#---------------------------------------------------------------------------------------------
# Zip the folder containing all images for easy download
!zip -r pdf_images.zip /content/pdf_images

# Provide the zipped images as a downloadable file
files.download("pdf_images.zip")
