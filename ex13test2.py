from sys import argv

script, name, age, origin = argv
print(">>> argv=", repr(argv))

print("what is your name?", end =' ')
name =input()
print("How old are you?", end = ' ')
age = input()
print("Where are you from?", end =' ')
origin =input()

print("Hi", name, f"you are {age} years old, and you come from {origin}")
