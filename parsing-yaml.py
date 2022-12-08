import yaml
from pprint import pprint

my_data = open("yaml_sample.yaml")
data_read = my_data.read()

print(data_read)


#convert to dictionary

yaml_dict = yaml.load(data_read, Loader=yaml.FullLoader)

pprint(yaml_dict)

# modify
yaml_dict["interface"]["ipv4"]["address"]["-ip"] = "192.168.0.10"

# print unparsed change
print(yaml.dump(yaml_dict, default_flow_style=False))

#write change

# open the fle in truncated mode
my_py_to_yaml = open("yaml_sample.yaml", "w")

# yaml to write
my_py_to_yaml.write(yaml.dump(yaml_dict, default_flow_style=False))

print(data_read)
