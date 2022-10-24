from sys import argv

myscript, input_file = argv

def print_all(file):
    print(file.read())

def rewind(file):
    print(file.seek(0))
    print("#" * 50)

def read_a_line(length_of_file, file):
    print(length_of_file, file.readline())
   

current_file = open(input_file)

print_all(current_file)

rewind(current_file)

#read_a_line(current_file)

print ("print 3 lines")

length_of_file = 1
read_a_line(length_of_file, current_file)

length_of_file  = length_of_file + 1
read_a_line(length_of_file, current_file)


length_of_file  = length_of_file + 1
read_a_line(length_of_file, current_file)

