from pprint import pprint
states ={"Victoria": "VIC",
         "New South Wales": "NSW",
         "Queensland": "QLD",
         "Australian Capital Territory": "ACT",
         "Western Australia": "WA",
         "Northern Territory": "NT",
         "South Australia": "SA"
}


cities_in_states ={"VIC": "Geelong",
                   "NSW": "Manly",
                   "QLD": "NewFarm",
                   "ACT": "Canbera",
                   "WA":  "Perth",
                   

}


#Add states
cities_in_states['SA'] = "Adelaide"
cities_in_states["NT"] = "Cairns"

pprint(cities_in_states)

#Lookup some cities belonging to statesusing the abbreviated keywords
print(f"SA state has {cities_in_states['SA']} city in its state")
print(f"NT state has {cities_in_states['NT']} city   in its state")
print(f"QLD state has {cities_in_states['QLD']} city  in its state")

#lookup some states and print their abbreviations
print("-" * 10)
print(f"Victoria's abbreviation is: {states['Victoria']}")
print(f"Queensland's abbreviation is: {states['Queensland']}")

#lookup by using states then cities dictionary
print("-" * 10)
print(f"Australian Capital territory has: {cities_in_states[states['Australian Capital Territory']]}")
print(f"South Australia has: {cities_in_states[states['South Australia']]}")

#print every state abbreviation
print("\n")
print("-" * 10)
for state, state_abbrev in list(states.items()):
    print(f"{state} has the abbreviation: {state_abbrev} ")

#print the city and its state abbreviation
print("\n")
print("-" * 10)
for city, state_abbrev in list(states.items()):
    print(">>> state_abbrev =", state_abbrev)
    print(f"{city} has {cities_in_states[state_abbrev]}")

#Lookup both state abbreviation and cites in state abbreviation at the same time
print("\n")
print("-" * 10)
for state, state_abbrev in list(states.items()):
    print(f"The state  {state} is abbreviated: {state_abbrev}")
    print(f"has {cities_in_states[state_abbrev]} as its city")

#print safely get an abbreviation for a state
state_search = states.get("Victoria")
print(states.get('Victoria'))
print(state_search)

state_search = states.get("Uluru")
print(state_search)

if not state_search:
    print("No Uluru sorry but no sorry")

city_search = cities_in_states.get("UL", "Uluru dioes not exist")

print(city_search)
print("\n")


#lookup keys in states dict
print("-" * 20)
print(states.keys())

#lookup values in states dict
print("-" * 20)
print(states.values())

#looking up both keys and values
print("-" * 20)
print(states.items())

#Adding elements using update dont know how
states.update({"Lagos":"Lag"})

#or 

#Adding using key value directly
states["Ogun"] = "ogun"
pprint(states)

#Deleting
print(states.popitem())

print("-" * 20)
pprint(states)
print(states.popitem())
