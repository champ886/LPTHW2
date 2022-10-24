from sys import argv
#from os.path  import exists

myScript, sourceFile, destFile = argv

print(f"copying files from {sourceFile} to {destFile}")

data_from_source = open(sourceFile)

data_from_source_open = data_from_source.read()



data_from_dest = open(destFile, "w")
data_from_dest.write(data_from_source_open)


