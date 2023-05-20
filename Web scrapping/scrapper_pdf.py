import requests
import os
from urllib.parse import urlparse, unquote
import certifi
from tqdm import tqdm

# Read the links from the file
with open('link_addresses_2.txt', 'r') as file:
    links = file.read().split(',')

# Create the folder to store the downloaded PDFs
folder_name = "Open Access Atlas of Otolaryngology, Head & Neck Operative Surgery | University of Cape Town (uct.ac.za)"
os.makedirs(folder_name, exist_ok=True)

# Loop through each link and download the PDF file
for link in tqdm(links, desc="Downloading", unit="file"):
    link = link.strip().strip("'")  # Remove leading/trailing spaces and single quotes

    # Extract the filename from the URL
    parsed_url = urlparse(link)
    unquoted_path = unquote(parsed_url.path)
    filename = unquoted_path.split('/')[-1] + '.pdf'

    # Modify the file name if it exceeds the maximum allowed length
    max_filename_length = 255  # Adjust as needed
    if len(filename) > max_filename_length:
        filename = filename[:max_filename_length - 4] + '.pdf'  # Truncate the file name and retain the .pdf extension

    # Construct the full path to check if the file exists
    file_path = os.path.join(folder_name, filename)

    # Check if the file already exists
    if os.path.exists(file_path):
        tqdm.write(f"File already exists: {filename}")
    else:
        # Download the PDF file
        try:
            response = requests.get(link, verify=certifi.where(), stream=True)
            if response.status_code == 200:
                # Save the PDF file in parts if it's too big
                chunk_size = 1024  # Size of each part (adjust as needed)
                total_size = int(response.headers.get('content-length', 0))
                progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=filename, ncols=80)
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        file.write(chunk)
                        progress_bar.update(len(chunk))
                progress_bar.close()
                tqdm.write(f"Downloaded: {filename}")
            else:
                tqdm.write(f"Empty file: {filename}")
        except requests.exceptions.RequestException as e:
            tqdm.write(f"Error downloading {filename}: {e}")
