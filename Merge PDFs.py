#---------------------------------------------------------------------------------------------
# Step 1: Install Required Libraries
#---------------------------------------------------------------------------------------------
!pip install PyPDF2

#---------------------------------------------------------------------------------------------
# Step 2: Import Necessary Libraries
#---------------------------------------------------------------------------------------------
from PyPDF2 import PdfReader, PdfWriter
from google.colab import files
import os

#---------------------------------------------------------------------------------------------
# Step 3: Upload Your PDF Files
#---------------------------------------------------------------------------------------------
uploaded = files.upload()  # Upload multiple PDFs to be merged

#---------------------------------------------------------------------------------------------
# Step 4: Merge the Uploaded PDFs
#---------------------------------------------------------------------------------------------
merger = PdfWriter()

# Loop through all uploaded files and add their pages to the merger
for pdf_name in uploaded.keys():
    reader = PdfReader(pdf_name)
    for page in range(len(reader.pages)):
        merger.add_page(reader.pages[page])

#---------------------------------------------------------------------------------------------
# Step 5: Save the Merged PDF
#---------------------------------------------------------------------------------------------
output_file = "/content/merged_output.pdf"
with open(output_file, "wb") as f_out:
    merger.write(f_out)

print(f"Merged PDF saved as {output_file}")

#---------------------------------------------------------------------------------------------
# Step 6: Download the Merged PDF
#---------------------------------------------------------------------------------------------
files.download(output_file)
