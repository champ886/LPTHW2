name = "champ nweke"
age = 35
height = 74
weight = 180
eye = "black"
teeth = "white"
hair = "black"
inches = 1.0
pound = 1.0

print (f"Let's talk about {name} ")
print (f"He is {age} years old")
print (f"He is {height} meters tall and wieghs about {weight} pounds")
print (f"He has {eye} eyes, {teeth} teeth")
print ( "and", hair, "hair" )

total = age + height + weight
print (f" if I add {age}, {height} and {weight}, I get a total of {total}")

convert_inches_to_cm = inches * 2.54
convert_pounds_to_kg = round(pound / 2.2406, 3)

print (f"1 inch converted to cm would be {convert_inches_to_cm} cnetimeters")
print (f"1 pound converted to kg would be {convert_pounds_to_kg} Kg")