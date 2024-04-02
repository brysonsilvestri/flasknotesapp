import requests

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/address/bill@gmail.com")
print(response.json())