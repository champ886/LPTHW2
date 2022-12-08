
import csv
from pprint import pprint


hostname = input("What is your hostname?")
ip = input("What is your IP address?")
location = input("What is the location?")

router = [hostname, ip, location]

with open("routerlist.csv", "a") as my_data:
    #use csv_writer variable below to set what data to write (my_data)
    write_to_csv = csv.writer(my_data)
    #write to csv with "csv.writer" 
    write_to_csv.writerow(router)

k = open("routerlist.csv")
y = list(k)
pprint(y)
