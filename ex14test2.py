from sys import argv

my_script, user_name = argv

prompt = "==> "

like =input(f"Do you like me {user_name}? \n{prompt}")


age = input(f"How old are you {user_name}?\n{prompt}")

print(f"Where do you live {user_name}?")
live =input(f"{prompt}")

print("What computer do you have?")
pc = input(prompt)

print(f"""
So you said {like} about liking me.
You are {age} years old.
You live in {live}. I know where that is.
And you have a {pc}... Nice!!
""")