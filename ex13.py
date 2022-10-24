from sys import argv
#read the WYSS section for how to run this
#unpacks argv module/feature and assigns it to 
#script, first, second, third as shown below:
script, first, second, third = argv

# Displaying contents of  the variable  called script
print("The script is called:", script)
# Displaying of the variable called first
print("Your first variable is:", first)
#Displaying contents of the variable called second
print("Your second variable is:", second)
#Displaying content of the variable called third
print(f"Your third variable is: {third}")