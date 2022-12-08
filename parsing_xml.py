import xmltodict
from pprint import pprint

with open("xml_sample.xml") as data:
    xml_sample_read = data.read()
print(xml_sample_read)

xml_dict = xmltodict.parse(xml_sample_read)

pprint(xml_dict)

#modify xml 

xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3"

#unparsed-- cached

print(xmltodict.unparse(xml_dict, pretty=True))

#to parse or write.. do below:

with open("xml_sample.xml", "w") as to_write:
    to_write.write(xmltodict.unparse(xml_dict, pretty=True))

print(xml_sample_read)