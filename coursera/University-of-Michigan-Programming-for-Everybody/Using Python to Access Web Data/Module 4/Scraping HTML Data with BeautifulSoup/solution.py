import urllib.request
from bs4 import BeautifulSoup

# Ask user for the URL
url = input('Enter - ')
html = urllib.request.urlopen(url).read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')

count = 0
total = 0

for tag in tags:
    # Extract the number inside <span> ... </span>
    num = int(tag.contents[0])
    total += num
    count += 1

print("Count", count)
print("Sum", total)
