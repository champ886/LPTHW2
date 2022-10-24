#++++++++++++ Display file content using ARGV module++++++++++++++##########
#import argv modules from python sys Package
from sys import argv

#Assign variables to argv
script, filename = argv

#Assign variable txt to open filename
txt = open(filename)

#An fstring statement/request to display variable "filename" content 
print(f"Here's ur file {filename}:")
#Print code below is to ACTUALLY READ and DISPLAY the content of 
# the "filename" above
print(txt.read())

#+++++++++++++++++++++ Re-Displaying file content  Again Using INPUT  fnction +++++++++++++++++++++++++++


#Re-display filename request
print("Type the filename again:")
#Code requests an input for filename
file_again = input("> ")

#This code assigns "txt_again" variable the inpput
#from the "file_again" request made above.
#The code below then assigns a new variable "txt_again",
# the task of "OPENING" the file

txt_again = open(file_again)

#this code reads and READS the content of the file again.. in this case ..
#"txt_again"
print(txt_again.read())