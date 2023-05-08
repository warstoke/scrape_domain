#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup

# Get the domain and word to search for from the command-line arguments
domain = sys.argv[1]
search_word = sys.argv[2]

# Send a GET request to the domain and get the HTML content
response = requests.get(domain)
html = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all links in the HTML content
links = soup.find_all('a')

# Loop through each link and check if it contains the search word
for link in links:
    href = link.get('href')
    if href:
        page_url = domain + href if href.startswith('/') else href
        page_response = requests.get(page_url)
        page_html = page_response.text
        if search_word in page_html:
            print(page_url)
