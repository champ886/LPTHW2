from os import write
from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("If you do not want that, please hit Control + C (^C).")
print("If you do want that, please hit RETURN.")

input("?")

target = open(filename)

print("Truncating the file ... Goodbye!!")
target.truncate

print("Now I am going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Now i am going to write to the files")

#target.write(line1, "\n", line2, "\n", line3)
target.write(f"{line1}\n{line2}\n{line3}")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)

print("I am now going to close it")
target.close()

