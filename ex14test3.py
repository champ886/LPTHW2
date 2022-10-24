from sys import argv
python_script_name, username = argv
question_prompt = f"{python_script_name} ({username}): "
print (f"Hi {username} I am {python_script_name}")
print (f"Do you like {username} ?")
likes = input(question_prompt)
print(likes)