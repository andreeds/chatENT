import requests
from bs4 import BeautifulSoup

# Define the website URL
website_url = 'https://health.uct.ac.za/entdev/guides/open-access-atlas-otolaryngology-head-neck-operative-surgery'

# Make a GET request to the website (with SSL verification disabled)
response = requests.get(website_url, verify=False)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the anchor tags that contain links to PDF files
pdf_tags = soup.find_all('a', href=lambda href: href and href.endswith('.pdf'))

# Extract the href attribute from each anchor tag and store in a list with single quotes
links = [f"'{tag['href']}'" for tag in pdf_tags]

# Save the links to a text file
filename = 'pdf_links.txt'
with open(filename, 'w') as file:
    file.write("links = [\n")
    file.write("    " + ",\n    ".join(links) + "\n")
    file.write("]")
