
file = open("openfile1demo.txt", 'w')

text1 =input("Type text:")
text2 = input("Type text2: ")
text3 = input("Type text3: ")

file.write(f"{text1}\n{text2}\n{text3}")

file = open("openfile1demo.txt", 'r')

print(file.read())