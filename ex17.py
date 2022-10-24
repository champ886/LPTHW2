from sys import argv, int_info
from os.path import exists

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

###+++++++++++++++++ Opening and reading  "from-file"+++++++++++++++++++##########
# We would do these two on one line, how?
in_file = open(from_file)


#Translation: in_file, cqan you please 
# read data from "from_file" and pass that variable to "indata" ?
indata = in_file.read()


print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

##++++++++++Opening t_file and copying data from "from_file" to "to_file"+++++#####
out_file = open(to_file, 'w')

out_file.write(indata)


print("Alright, all done.")


out_file.close()
in_file.close()