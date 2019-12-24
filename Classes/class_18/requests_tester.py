import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

json_data = response.text

decoded = json.loads(json_data)

print(decoded)
print(type(decoded))

