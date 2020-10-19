import json
from pprint import pprint
currency = {"Country": "India", "Currency": "Rupee"}

json_var = json.dumps(currency)
print(json_var)
print(type(json_var))

with open("data_file/currency.json","a") as curr:
    curr.write(json_var)
    

    





