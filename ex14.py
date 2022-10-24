#imports argv module from python sys
from sys import argv
#Assigns scripy and username to argv
script, user_name = argv
#Creates a variable called prompt to prompt users
prompt = f"{script}:  ({user_name})> "


#Display using username and script variable unpacked argv
print(f"Hi {user_name}, I'm the {script} script.")
#Prints questions
print("I'd like to ask you a few questions.")
#Display string test using Username variable unpacked form argv .. again
print(f"Do you like me {user_name}")
#likes variable is assigned whatever content is gotten from the input(prompt) variable
likes = input(prompt)

#Dispalys username.. again
print(f"Where do you live {user_name}?")
#Lives variable is assigned whatever content is gotten from the prompt variable during input
lives = input(prompt)

print(f"How old are you {user_name}")
age = input(prompt)
print(">>> age=", repr(age))
#printing text to ask for PC type
print(f"you're {int(age)}. What kind of computer do you have?")

#Computer is also assigned whatever content is gotten from the prompt variable during input
computer = input(prompt)

#Displays a text that puts all prompts and arguments together
print(f"""
Alright, so you said {likes} about liking me.
You are {age} years old.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")