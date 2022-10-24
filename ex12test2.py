name = input("What is your name: ")
country = input("What country are you from: ")
current_address = input("Where do you currently live: ")
age = float(input("How old are you: "))


print(f"""
My name is {name},
I am {age} years old.
I am from {country},
but currently live in """, current_address)