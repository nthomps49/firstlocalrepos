import requests
from pprint import pprint
import json
#print(requests.__version__)
#print(requests.__copyright__)
r_get = requests.get('http://www.metaweather.com/api/location/2436704/2020/10/06/')#this website allows get requests without authentication.
#print(r_get)
#print(r_get.status_code)- gives 200 Successful
#print(type(r_get))
#print(type(r_get.headers))
#pprint(r_get.headers)# shows  'Allow': 'GET, HEAD, OPTIONS' so not all http requests allowed
#print(r_get.text)- mass jumbled information
data = json.loads(r_get.text)
pprint(data)
#you can use www.woeidlookup.com - where on earth identifier to get different location IDs.
#r_get.is_redirect will tell you if the URL is a redirect - this example is false
