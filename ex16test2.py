from sys import argv
from os import write

myScript, filename = argv

file = open(filename, "w")

print("opening and truncating file...")
print("Please press 'ctrl + c' to abort....")
print("Press 'Enter' to continue.... \v")

print("Emptying the file... goodbye")
#file.truncate(1)

print(" enter the following lines...\v")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

file.write(f"{line1}\n{line2}\n{line3}")
