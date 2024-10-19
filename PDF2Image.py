#---------------------------------------------------------------------------------------------
# Step 1: Install Required Libraries
#---------------------------------------------------------------------------------------------
!pip install pdf2image
!apt-get install poppler-utils

#---------------------------------------------------------------------------------------------
# Step 2: Import Necessary Libraries
#---------------------------------------------------------------------------------------------
from pdf2image import convert_from_path
from google.colab import files
import os

#---------------------------------------------------------------------------------------------
# Step 3: Upload Your PDF File
#---------------------------------------------------------------------------------------------
uploaded = files.upload()

#---------------------------------------------------------------------------------------------
# Step 4: Convert the Uploaded PDF to Images
#---------------------------------------------------------------------------------------------
pdf_file = list(uploaded.keys())[0]
images = convert_from_path(pdf_file, dpi=400)

#---------------------------------------------------------------------------------------------
# Step 5: Save the Images
#---------------------------------------------------------------------------------------------
output_dir = "/content/pdf_images"
os.makedirs(output_dir, exist_ok=True)

for i, image in enumerate(images):
    image_path = f"{output_dir}/page_{i + 1}.png"
    image.save(image_path, "PNG")
    print(f"Saved {image_path}")

#---------------------------------------------------------------------------------------------
# Step 6: Download the Images
#---------------------------------------------------------------------------------------------
!zip -r pdf_images.zip /content/pdf_images
files.download("pdf_images.zip")

