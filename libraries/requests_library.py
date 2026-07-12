import requests

url = "https://www.google.com/"

response = requests.get(url, timeout=5)

print(response.text)