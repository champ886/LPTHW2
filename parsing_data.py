from pprint import pprint
import csv

# open csv ==> open --> csv.reader --> list

samplefile = open("routerlist.csv")
samplereader = csv.reader(samplefile)
sampledata = list(samplereader)

pprint(sampledata)

print("*" * 50)

pprint(sampledata[0])


print("*" * 50)

pprint(sampledata[1])


print("*" * 50)

pprint(sampledata[0][1])
pprint( sampledata[0][2])
print("*" * 50)

pprint(sampledata[0][0])


print("*" * 25, "Using 'with'", "*" * 25)

with open("routerlist.csv") as samplefile01:
    samplefile_read = csv.reader(samplefile01)
    samplefile_list = list(samplefile_read)
    pprint(samplefile_list)

for row in samplefile_list:
    # different from sampledata[0], as for is looping through the whole list
    device = row[0]
    location = row [2]
    ip_addr = row[1]

    print(f"{device}, is in {location.rstrip()}, and has ip address {ip_addr.rstrip()}")