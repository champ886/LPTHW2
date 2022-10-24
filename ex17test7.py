from sys import argv, int_info
from os.path import exists

myscript, current_file, dest_file = argv

open_file = open(current_file)

read_file = open_file.read()

print(f"The {myscript} file is {len(read_file)} bytes long")

print(f" Does the {dest_file} exist ?", exists(dest_file))

print(""" Do you want to copy file to another ?
hit enter to continue, or ctrl + c to exist this script""")
input ("continue ?: ")

current_file_open_and_truncate = open(dest_file, "w")

dest_file_write = current_file_open_and_truncate.write(read_file)
