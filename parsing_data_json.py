
import json
from pprint import pprint
with open("json_sample.json") as data:
    json_data = data.read()
    
#json_dict = json.loads(json_data)
print(json_data)

print("\n")
my_data = open("json_sample.json")
read_data = my_data.read()

print(read_data)

json_my_dict = json.loads(read_data)

pprint(json_my_dict)

json_my_dict["interface"]["description"] = "Backup Link"


pprint(json_my_dict)


# Write to json file 
with open("json_sample.json", "w") as my_data01:
    json.dump(json_my_dict, my_data01, indent = 0)