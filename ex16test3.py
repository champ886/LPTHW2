from os import write
from sys import argv

pythonScript, filename = argv

print("We are going to erase ", filename)

print("if you do not want that, hit ctrl + C")
print ("if you do not want that, hit return (enter)")
input ("?: ")

print("opening the file")

target = open(filename, "w")

print("Truncating the file")

print("Now I am going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

target.write(f"{line1}\n{line2}\n{line3}\n")
target.close()