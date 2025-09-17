import urllib.request
import xml.etree.ElementTree as ET

# Prompt for URL
url = input("Enter location: ")

print("Retrieving", url)
data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

# Parse XML
tree = ET.fromstring(data)

# Find all <count> elements
counts = tree.findall('.//count')

# Convert text to integers
nums = [int(c.text) for c in counts]

print("Count:", len(nums))
print("Sum:", sum(nums))
