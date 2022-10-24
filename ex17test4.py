from sys import argv

myscript, sourceFile, destFile  = argv

print(f"copying from file {sourceFile} to {destFile}")

data_from_source = open(sourceFile, "r")
print(data_from_source.read())


#data_from_dest = open(destFile, "w")
#data_from_dest.write(data_from_source)

    