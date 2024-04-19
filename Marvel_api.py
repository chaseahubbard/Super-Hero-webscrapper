public_key = 'e2013c505292cae3c62bc04d723ddec6'
private_key = '1be747ef3d002dc41de237b9ec2f2edc645c51d9'



import hashlib
import requests
from requests.auth import HTTPDigestAuth
import json
import time
from PIL import Image
from io import BytesIO
ts = str(time.time())
hash_value = ts + private_key + public_key

hash_value = hashlib.md5(hash_value.encode()).hexdigest()
topic = 'characters'

request_url = 'http://gateway.marvel.com/v1/public/' + topic

params = { 'apikey': public_key,
    'ts': ts,
    'hash': hash_value,
    'name': 'Wolverine'}

myResponse = requests.get(request_url, params=params)


data = myResponse.json()

if myResponse.status_code == 200 :
    if data['data']['results']:
        wolverine_info = data['data']['results'][0]  # Assuming Wolverine is the first result
        print("Name:", wolverine_info['name'])
        print("Description:", wolverine_info['description'])
        thumbnail_url = wolverine_info['thumbnail']['path'] + '.' + wolverine_info['thumbnail']['extension']
        print("Thumbnail URL:", thumbnail_url)
        
        # Fetch and display the image
        image_response = requests.get(thumbnail_url)
        img = Image.open(BytesIO(image_response.content))
        img.show()
    else:
        print("Wolverine not found.")
else:
    # Print an error message if the request was not successful
    print("Error:", myResponse.status_code)

''' 
if myResponse.status_code == 200 :

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
        print (str(key) + " : " + str(jData[key]))
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()
'''