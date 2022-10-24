#++++++++++++++++ Code to Overwrite a file +++++++++++++++++++++#

#import write module form python OS package
from os import write
#import argv module from python sys pckage
from sys import argv

#Assign variables Script and filename to argv module
script, filename = argv

#Displaying string sentence to erase "filename" 
print(f"We're going to erase {filename}.")
#Displaying an option to stop 
#with Control + C to kill script if not wanting to go ahead
print("If you don't want that, hit CTRL-C (^C).")
#Displaying text to chose to continue "Enter"
print("If you do not want that, hit RETRUN.")

#Input string to accept option above, to coninue or stop
input("?")

#Display action of opening file
print("Opening the file....")
#Open file and assign to target
# researching the use of 'w' W = for truncating file first before writing
target = open(filename, 'w')

#to empty or clean out the file
print("Truncating the file.  Goodbye!!")
#"target.truncate" below not necessary when using 'w' above
#target.truncate

#Display text to write lines to file
print("Now I am going to ask you for three lines.")

#variables line1-line3 take input from user
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#Displaying test to show that the above will be written to file
print("I'm going to write these to the file.")

#Writing input from lines1-3 to file using contents of variable "target" above,
#..(which was an open file)  to overwrite 3 new lines in file "filename"
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")  OR Below:

target.write(f"{line1}\n{line2}\n{line3}")


#files successfully overwritten and closed
print("And finally, we close it.")
target.close()