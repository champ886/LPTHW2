from sys import argv, int_info
from os.path import exists

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

###+++++++++++++++++ Opening and reading  "from-file"+++++++++++++++++++##########
# We would do these two on one line, how?
#In order to read/write/truncate/etc a file ==> IT NEEDS TO BE OPEN FIRST
in_file = open(from_file, 'r')
print(">> in_file=", repr(in_file))

indata = in_file.read()
#print(">> indata=", repr(indata))


#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

##++++++++++Opening t_file and copying data from "from_file" to "to_file"+++++#####
out_file = open(to_file, 'w')
#print(">>> out_file=", repr(out_file))
out_file.write(indata)
#print(">>> out_file.write=", repr(out_file.write))

print("Alright, all done.")

out_file.close()
in_file.close()