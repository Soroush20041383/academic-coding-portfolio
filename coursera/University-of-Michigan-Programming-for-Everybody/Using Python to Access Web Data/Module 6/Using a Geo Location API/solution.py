import urllib.request, urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    parms = dict()
    parms["q"] = address
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "features" not in js or len(js["features"]) == 0:
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    # The JSON structure is: features[0]["properties"]["plus_code"]
    plus_code = js["features"][0]["properties"]["plus_code"]
    print("Plus code", plus_code)
