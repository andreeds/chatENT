import os
import pdfcrowd

# PDFcrowd credentials
username = 'andreeds'
api_key = '0bdf24065b7fa12021c879c37b553d09'

# Read URLs from file
with open('link_addresses.txt', 'r') as file:
    urls = [url.strip() for url in file.readlines()]

# Create output directory if it doesn't exist
output_dir = 'Iowa Head and Neck Protocols (uiowa.edu)/PDF'
os.makedirs(output_dir, exist_ok=True)

# Initialize PDFcrowd client
client = pdfcrowd.HtmlToPdfClient(username, api_key)

# Convert URLs to PDFs
for url in urls:
    try:
        # Generate PDF from URL
        output_file = os.path.join(output_dir, f'{url.split("/")[-1]}.pdf')
        client.convertUrlToFile(url, output_file)
        print(f"Successfully converted {url} to {output_file}")
    except pdfcrowd.Error as why:
        # Handle PDFcrowd errors
        print(f"Error converting URL: {url}. {why}")

# Close the PDFcrowd client
client.close()
