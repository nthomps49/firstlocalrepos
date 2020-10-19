import json
from pprint import pprint

dessert = {"Name": "Ice cream", "Flavours": ["Chocolate", "Pineapple"], "Toppings":True, "WaffleCone": "Yes" }
print(dessert)
dessert_str = json.dumps(dessert, indent = 2, separators=(":","="),sort_keys=True)
print(dessert_str)

with open('data_file/eat.txt','w') as json_file:
    json.dump(dessert, json_file)