import requests

response = requests.get('127.0.0.1:8000/drinks')
print(response.json())
