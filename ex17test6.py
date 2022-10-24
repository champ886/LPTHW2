from  sys import argv, int_info
from os.path import exists

myscript, current_file, dest_file = argv

print(f"copy from {current_file} to {dest_file})")

open_file = open(current_file)

read_file = open_file.read()


print ("press enter to continue or press ctrl + c to quit")
input ("continue ?: ")

copy_content_old_file = open(dest_file, "w")

write_to_new = copy_content_old_file.write(read_file)
