import json
import requests

url = 'https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/v1'
fruit = 'Apple'
color = 'Red'
final_url = f'{url}/fruit/{fruit}'

response = requests.get(final_url, params={'color': color}).json()

print(json.dumps(response, indent=4))