from sys import argv

myScript, filename = argv

txt = open(filename)

print("Here is the content of your file ", filename)

print(txt.read())
