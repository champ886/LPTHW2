from sys import argv, int_info
from os.path import exists

myscript, from_file, to_file = argv

print(f"copying {from_file} to {to_file}")

in_file=open(from_file)

read_file = in_file.read()

print(f"the input file is {len(read_file)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")

print("Ready hit enter to continue and ctrl + C to abort")
input("continue ?: ")

out_file = open(to_file, "w")
out_file.write(read_file)

print("Alright all done")