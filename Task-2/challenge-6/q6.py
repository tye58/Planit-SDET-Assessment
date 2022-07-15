import requests
import json

response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
print('The response status code is', response.status_code)

pet_list=response.json()
print('The number of pets is', len(pet_list))


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

#jprint(response.json())