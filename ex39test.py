from pprint import pprint

#Creates a mapping of a state to abbreviation
#Key = state, Value = Abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#Create a basic set of states and some cities in them
# Key = States, Value = Cities
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
#Syntax dict['Key'] = value
cities['NY'] = 'New York'
cities["OR"] = 'Portland'

#print out some cities
# Print a dash 10 times
# Print NY and Oregon cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print out some states
#print dash 10 times for spacing
#Print abbreviations in states Michigan and Florida
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do it by using state then cities dict
#Print dash 10 times for spacing
#Print states, then print cities belonging to Michigan and Florida states
print('-'*10)
city = states['Michigan']
print(">>> Michigan states=", city)
print("Michigan has: ", cities[city])
print("Florida has: ", cities[states['Florida']])

#Print every state abbreviation
# Using key value display or sorting
# eg: Michigan (key /State), MI(value/abbrve),
print('-' * 10)
for i in list(states.items()):
    print(">>> loop i=", repr(i))
    state, abbrev  = i
    print(f"{state} is abbreviated {abbrev}")

#print the city and (key) and abbreviation (value) in state dictionary
#using key/value lookup

print('-' * 10)
for city, abbrev in list(states.items()):
    print(f"{city} has the city {abbrev}")

#now do both at the same time
print('-' * 10)
# The below lists the Key and values (Key:Values) in states dict
# in a comma seperated manner .lineally
# using python method "Items()"
#With each key-value pair assigned to variables 
#==> state and abbrev in the for loop below
for i in list(states.items()):
    state, abbrev = i
    print(">>> loop i =", i)
    print(f"{state} state is abbreviated {abbrev}")
    print(">>> state=", state, "abbrev=", abbrev)
    #Passes  the value (Or content) of abbrev "key"  to "cities" dictionary.. How?
    # Eg dict cities, 'CA" = 'San Francisco' CA =key: San Francisco = Value
    # Therefore cities call the value of an abbreviation, in this case San Francisco
    print(f"and has city {cities[abbrev]}")
    print(">>> cities[abbrev] =", cities[abbrev])
    print(">>> cities =", cities, 'abbrev =', abbrev)

print('-' * 10)
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas")

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")


print("\n")
#+++++++++++++++++++++++++++

pprint(states.items())

pprint(cities.items())

print(states)



for abbrev, city in list(cities.items()):
    print("The abbreviation is  ", abbrev, "its city is  ", city)
    print(f"The city is {cities[abbrev]} ")