name = 'Champ Nweke'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Brown'
inches = 1.0
pounds = 1.0

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on bitter cola")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

convert_inches_to_Cm = inches * 2.54
convert_Pounds_to_Kg = round(pounds / 2.2046, 3)
print (f"1 inch converted to centimeter would be {convert_inches_to_Cm} centimetres")
print (f"1 pound converted to kg would be: {convert_Pounds_to_Kg} kilograms")