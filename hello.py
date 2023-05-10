import requests

if requests.get("https://www.google.com"):
    print("Success")
else:
    print("Darn")
