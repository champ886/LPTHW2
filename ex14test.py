from sys import argv

script, user_name = argv

prompt = f"{script}:  "

print(f"Hi {user_name}, I am the {script} script.")
print("I would like to ask you a few questions.")
like = input(f"Do you like me {user_name}? \n{prompt}")
#like = input(prompt)

print(f"Where do you live {user_name}? ")
live = input(prompt)

print(f"What sort of computer do you have?")
computer = input(prompt)

age = input(f"How old are you {user_name}? \n{prompt} ")
#age =input(prompt)

print(f"""
Ok.. So you said {like} about liking me.
You are {age} years old..... Really?
You live in {live}.  Hmmmm.. Not sure where that is.
And you have a {computer} computer.. Nooice!! 
""")