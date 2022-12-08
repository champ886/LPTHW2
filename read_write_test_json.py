import json
from pprint import pprint

my_data= open("test_json.json")
my_data_read = my_data.read()


print(my_data_read)

# assign to dictionary in python

my_dict =json.loads(my_data_read)

pprint(my_dict)

# edit json file

my_dict["interface"]["ipv4"]["address"].insert(0, "ip:" "192.168.20.5")

pprint(my_dict)

#write from python to json

#with open("test_json.json", "w") as my_data01:
 #  json.dump(my_dict,my_data01)
   

print(my_data_read)