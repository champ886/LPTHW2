states = {
    "Lagos" : 'LG',
    "Edo" : "ED",
    "Enugu" : "EN",
    "Victoria" : "VIC",
    "Queensland": "QLD"

}

cities = {
    "LG" : "Ikeja",
    "ED" : "Benin",
    "EN" : "Enugu"
}

cities["VIC"] = "Melbourne"
cities["QLD"] = "Brisbane"



print("_" * 50)
print("Victoria has: ", cities["VIC"])
print("Queensland has :", cities["QLD"])

print("_" * 50)
print("Lagos' abbreviation is: ", states["Lagos"])
print("Edo's abbreviation is: ", states["Edo"])

print("_" * 50)
print ("Print every state")
print(list(states.items()))
for state, abbrv in list(states.items()):
    print(f"{state} is abbreviated {abbrv}")

print("_" * 50)
print ("Print every city")
for abbrv, city in list(states.items()):
    print(f"{abbrv} is {city}")

print("$" * 50)


for state, abbrv_city in list(states.items()):
    print(f"{state} is {abbrv_city}")
    print(f" and has: {cities[abbrv_city]}")

state = states.get("Jagun")

if not state:
    print("Sorry, not Jagun")


a = cities.get("LG")
print(a)


IT ={
    "Aruba" : "wifi",
    "Cisco" : "router",
    "Palo": "Firewall"
}

b = IT.items()

for a, v in b: #IT.items():
    print(a,v)

d = IT.get(" ")
print(IT)


for abbrv_city, city in list(cities.items()):
    print (f"{city} belongs to {abbrv_city}")

for key, value in list(states.items()):
    print(f"State {key} has abbrevaition: {value} ")
    print (f"and has a city of {cities[value]} ")


#Dict[Key] = "value"
states["New york"] = "NY"

print(states)