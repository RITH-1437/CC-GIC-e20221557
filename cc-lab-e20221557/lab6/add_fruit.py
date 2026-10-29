import json
import requests

url = 'https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/v1'

new_fruit = {
    'name': 'Grapes',
    'color': 'Green',
    'flavor': 'Sour'
}

final_url = f'{url}/fruit'

print("POST request payload:")
print(json.dumps(new_fruit, indent=4))

response = requests.post(final_url, json=new_fruit)

print("\nPOST status code:", response.status_code)
print("POST response:")
print(response.text)