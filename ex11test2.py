print("Where are you from: ", end = "")
country = input()
print("What is your name: ", end ="")
name = input()
print("Where do you currently live: ")
address_current = input()
print("How old are you: ")
age = float(input())

#troubleshoot
print(">>> age", age)

print(f""" 
My name is {name}
I am {age} years old
I am from {country}
and I currently reside in """, address_current)