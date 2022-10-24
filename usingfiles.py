#from sys import argv
#myScript, myFile =argv
#from os.path import exists

f = open("/home/champ/Desktop/Python_Training_LPTHW/readtext.txt", "r+")
print(f.read())

f.write("\n yo yo")
print(f.read())
f.close()