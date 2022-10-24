#Using input to read file

filename = input("Type in your file name:> ")

txt = open(filename)

print(txt.read())