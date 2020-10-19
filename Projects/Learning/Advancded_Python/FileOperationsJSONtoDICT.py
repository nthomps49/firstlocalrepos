import json
from pprint import pprint
with open("data_file/currency.json") as curr:
    currency_dict = json.load(curr)
pprint(currency_dict)
print(type(currency_dict))






