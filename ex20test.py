# import argv from sys module
from sys import argv

# Assign script and input_file variable to argv
script, input_file = argv

##########  DEFINING FUNCTIONS FIRST ##########################################
# Defining print_all function==> to read file


def print_all(f):
   # print(">>> print_all: f=", f)
    print(f.read())
   # print("<<< print_all: f=", f)

# defining rewind file function==>
#  to  seek postion on file (defines where data has to be read or written to in a file)


def rewind(f):
    #print(">>> rewind: f=", f)
    f.seek(0)
    #print("<<< rewind: f=", f)

# define function with linecount and f parameters==>
# Function action ==> to read one complete line (readline)
#  and to count line (line count)


def print_a_line(line_count, f):
    #print(">>> print_a_line line_count=", line_count, "f=", f)
    print(line_count, f.readline())
    #print(">>> print_a_line line_count=", line_count, "print_a_line f=", f)


####++++++++++++++ Writing code +++++++++++############################

# Define variable current_file to open any file from argument(argv)
current_file = open(input_file)

# Prints the whole file
print("First let's print the whole file:\n")

# Prints current file ==> using the "print_all" function
# by passing the content of the variable to function ==>
# "print_all(f)"
print_all(current_file)

# rewinds current file using the "rewind" function
print("Now let's rewind the tape")
# by passing the content of the variable to function ==>
# "print_all(f)"
rewind(current_file)

# Prints three lines ==> using the print_a_line function below:
print("Let's print three lines:")

# ||
# ||
# V

# Prints first line
# Current_line variable passes argument to "line_count" parameter in function above
current_line = 1
# current_line ==> for the current line
# current_file ==> reads each line respectively due to function action ==>
# print_a_line action ==> f.readline()
print(">>> current_line =", repr(current_line))
print_a_line(current_line, current_file)

# Prints line 2 using increments (+1)
# cuurent_line = +1 ==> Menaning below:
# ##1. Adds another value (+1) to the variable's value ==>
# ###which is 1( as above (current_file = 1)
# ##2. Assigns the new value to the variable ==> current_file
# Hence current_line = 2
current_line += 1  # (Or current_file + 1)
print(">>> current_line =", repr(current_line))
print_a_line(current_line, current_file)

# Prints line 3 using incrememnts (+1)
#current_line = 3
current_line += 1  # (or current_file + 1)
print(">>> current_line =", repr(current_line))
print_a_line(current_line, current_file)
