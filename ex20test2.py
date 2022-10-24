from sys import argv

myScript, myFile = argv

def print_all(f):
    print(f.read())

def rewind(f):
    (f.seek(0))

def print_line(linecount, f):
    print(linecount, f.readline())

file_input = open(myFile)

print_all(file_input)

print("Rewind file: ")

rewind(file_input)
print('Print The lines below: ')

current_line = 1

print_line(current_line, file_input)

current_line = current_line + 1
print_line(current_line, file_input)

current_line += 1
print_line(current_line, file_input)





