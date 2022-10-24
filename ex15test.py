from sys import argv

script, filename = argv

#Defines key variables to be used to read and open text
txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again: ")

#Defines key variable to be used read and open text
read_a_txt_again = input(">: ")

file_again = open(read_a_txt_again)

print(file_again.read())