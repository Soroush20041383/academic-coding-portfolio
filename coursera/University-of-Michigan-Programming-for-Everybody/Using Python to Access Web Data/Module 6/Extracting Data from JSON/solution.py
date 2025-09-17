import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving", url)

# Read data from the URL
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

# Load JSON
info = json.loads(data)

# Navigate into the 'comments' list
comments = info["comments"]

# Extract counts
counts = [int(item["count"]) for item in comments]

print("Count:", len(counts))
print("Sum:", sum(counts))
