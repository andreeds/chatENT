import requests
from bs4 import BeautifulSoup

# Define the website URL
website_url = 'https://medicine.uiowa.edu/iowaprotocols/head-and-neck-oncology-home-page'

# Make a GET request to the website
response = requests.get(website_url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the anchor tags that contain links
anchor_tags = soup.find_all('a')

# Extract the href attribute from each anchor tag and store in a list with single quotes
links = [f"'{tag['href']}'" for tag in anchor_tags if 'href' in tag.attrs]

# Filter out empty and non-HTTP links
links = [link for link in links if link.startswith("'http")]

# Save the links to a text file
filename = 'link_addresses.txt'
with open(filename, 'w') as file:
    file.write("links = [\n")
    file.write("    " + ",\n    ".join(links) + "\n")
    file.write("]")
