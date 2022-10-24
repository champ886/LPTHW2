from os import write

from sys import argv

myscript, filename = argv

content = open(filename, "r")
print(content.read())
print("."* 30)
print(f" we are opening {filename}")
print (f"Truncating file... {filename}")

print ("To stop truncating press ctrl + C")

print ("TO continue, hit enter")

input("(Continue)?: ")


target =open(filename, "w")

print("Enter three lines of text")


line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

target.write(f"{line1}\n{line2}\n{line3}\n")

print(target)
print(target.close())
print(filename)


target_again = open(filename)
print("  " * 30)
print("*" * 30)
print("Final content of file is:")
print(target_again.read())


