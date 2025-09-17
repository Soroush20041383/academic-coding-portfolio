import urllib.request
from bs4 import BeautifulSoup

# Inputs
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

print("Retrieving:", url)

for i in range(count):
    # Fetch the HTML
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Get all anchor tags
    tags = soup('a')

    # Pick the tag at the given position (1-based index)
    tag = tags[position - 1]
    url = tag.get('href', None)
    print("Retrieving:", url)

# Extract and print the last name from the final URL
print("The answer to the assignment is:", url.split('_')[-1].replace('.html', ''))
