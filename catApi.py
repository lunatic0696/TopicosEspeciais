import requests
import random

api_key = "MzA0MDU1"
url = 'http://thecatapi.com/api/images/get'
image_id = random.randint(1,1000)
print(url)
print(image_id)

response = requests.get(url, headers = {'api_key' : api_key, 'image_id' : image_id}).json()