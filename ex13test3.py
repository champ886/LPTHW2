from sys import argv

myscript, value1, value2, value3 = argv

value1 = input("What is your name?: ")
value2 = input(("How old are you?: "))
print ("Where is your dad from? :", end =" ")
value3 = input()

print(f"So your name is {value1}, you are {value2} years old,"
"Your dad is from", value3)