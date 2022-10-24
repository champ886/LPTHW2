from sys import argv

myScript, sourceFile, destFile = argv

print(f"Copying files from {sourceFile} to {destFile}")
print(">>>", sourceFile, destFile)

data_from_source = open(sourceFile)
print(">>> ", data_from_source, sourceFile)
data_from_source_openned = data_from_source.read()
print(">>>", data_from_source_openned, data_from_source)

data_from_dest = open(destFile, "w")
print(">>>", data_from_dest, destFile)
data_from_dest.write(data_from_source_openned)
print(">>>", data_from_dest, data_from_source_openned)
