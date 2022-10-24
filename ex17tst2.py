from sys import argv
from os.path  import exists

myScript, sourceFile, destFile = argv

print(f"writing files from {sourceFile} to {destFile}")
