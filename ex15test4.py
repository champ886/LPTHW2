from sys import argv

python_script, filename = argv

txt = open(filename)

print(f"Here is your {filename}: ")

print(txt.read())

print("Type the filname again: ")
filename_again = input()

txt_again = open(filename_again)

print(txt_again.read())