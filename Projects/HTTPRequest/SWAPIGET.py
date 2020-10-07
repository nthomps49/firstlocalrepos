import requests
from pprint import pprint
import json

r_get = requests.get('http://swapi.dev/api/vehicles/14')
#print(r_get)
#pprint(r_get.headers)
#print(r_get.text)
data = json.loads(r_get.text)
pprint(data)
