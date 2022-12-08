from pprint import pprint
with open ("json_sample.json") as my_data:
    json_read = my_data.read()
    pprint(json_read)