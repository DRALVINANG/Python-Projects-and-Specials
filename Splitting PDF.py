#---------------------------------------------------------------------------------------------
# Step 1: Install Required Libraries
#---------------------------------------------------------------------------------------------
!pip install PyPDF2  # Install PyPDF2 library for PDF manipulation

#---------------------------------------------------------------------------------------------
# Step 2: Import Necessary Libraries
#---------------------------------------------------------------------------------------------
from PyPDF2 import PdfReader, PdfWriter
from google.colab import files
import os

#---------------------------------------------------------------------------------------------
# Step 3: Upload Your PDF File
#---------------------------------------------------------------------------------------------
uploaded = files.upload()

#---------------------------------------------------------------------------------------------
# Step 4: Load the PDF and Prepare for Splitting
#---------------------------------------------------------------------------------------------
pdf_file = list(uploaded.keys())[0]  # Get the uploaded PDF filename
reader = PdfReader(pdf_file)  # Load the PDF file

print(f"Number of pages in the PDF: {len(reader.pages)}")

#---------------------------------------------------------------------------------------------
# Step 5: Define the Page Ranges for Splitting
#---------------------------------------------------------------------------------------------
# Example: Split into two PDFs (pages 1-3 and 4-end)
split_ranges = [(0, 2), (3, len(reader.pages) - 1)]  
# Python index starts at 0

#---------------------------------------------------------------------------------------------
# Step 6: Split and Save the PDFs
#---------------------------------------------------------------------------------------------
output_dir = "/content/split_pdfs"
os.makedirs(output_dir, exist_ok=True)

for i, (start, end) in enumerate(split_ranges):
    writer = PdfWriter()
    for page_num in range(start, end + 1):
        writer.add_page(reader.pages[page_num])
    output_file = f"{output_dir}/split_{i + 1}.pdf"
    with open(output_file, "wb") as f_out:
        writer.write(f_out)
    print(f"Saved {output_file}")

#---------------------------------------------------------------------------------------------
# Step 7: Download the Split PDFs
#---------------------------------------------------------------------------------------------
!zip -r split_pdfs.zip /content/split_pdfs
files.download("split_pdfs.zip")
