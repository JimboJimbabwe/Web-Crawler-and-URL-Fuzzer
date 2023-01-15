import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

var = input("Enter the URL to crawl: ")

def crawl(var):
    # Make a request to the website
    response = requests.get(var)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the links on the page
    links = soup.find_all('a')

    # Open a file for writing
    with open('urls.txt', 'w') as f:
        # Write the links to the file
        for link in links:
            # Use the urljoin function to combine the base URL with the link
            full_link = urljoin(var, link.get('href'))
            f.write(full_link + '\n')

# Call the crawl function with the URL as the argument
crawl(var)

# Open the file for reading
with open('urls.txt', 'r') as f:
    # Read the links from the file
    urls = f.readlines()

# Read the list of paths from the file
with open('paths.txt', 'r') as f:
    paths = f.readlines()

# Iterate through the list of URLs
for url in urls:
    # Strip leading/trailing whitespace from the URL
    url = url.strip()
    for path in paths:
        path = path.strip()
        new_url = url + path
        # Send an HTTP GET request to each new URL
        response = requests.get(new_url)

        # Check if the status code is 200
        if response.status_code == 200:
            print(f'{new_url} returned status code 200')
        else:
            print(f'{new_url} returned status code {response.status_code}')
