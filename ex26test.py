from sys import argv

print("How old are you")
age = input()


print ("How tall are you? ")
height = float(input())

address = str(input("Where do you live ?\n"))

weight = float(input("How much do you weigh?\n"))
print (f"So you are {age} years old, {height} meters tall {weight} kg heavy and live in {address}")

myscript, filename = argv

txt = open(filename)
read_file = txt.read()
print(f"Here is our file {filename}")
print(read_file)

#print("Type the filename again")
txt_file_again = input("Type the file name again")
txt_open_again = open(txt_file_again, 'a')
#print(txt_open_again.read())



def secretformula(started):
    jelly = started * 1000
    jar = jelly / 100
    beans = jar * 50
    return jelly, jar, beans

def print_items(started):
    jelly, jar, beans = secretformula(started)
    print(f" we'd have {jelly} jelly, {beans} bean {jar} jar")

start_point = 1000
secretformula(start_point)
print(f" with a start point of {start_point}")
print_items(start_point)
#print(f"we'd have {beans} beans, {jar} jars and {jelly} jellies")

start_point = start_point / 100
formula = secretformula(start_point)

print(f"With a start point of {start_point}")
print("we'd have {} beans, {} jars and {} jellies".format(*formula))

people = 20
cats = 50
dog = 10

if people < cats:
    print("The world is doomed")

if cats > people:
    print("The world is still in trouble")

if people > cats:
    print("Ahhh.. good stuff")

if people < dog:
    print("The world is drooled on")

if people > dog:
    print ("The world is normal")

dog = dog + 10

print(">>>", dog)

if people >= dog:
    print(">>> people", people, ">>> dog", dog)
    print("People are greater than or equal to dogs")

if people < dog:
    print(">>> people", people, ">>> dog", dog)
    print("oh no not again!")

if people == dog:
    print(">>> people", people, ">>> dog", dog)
    print("people are dogs")

content_myscript = open(myscript)
read_myscript = content_myscript.read()
print (read_myscript)

txt_open_again.write(read_myscript)
print(txt_open_again.write(read_myscript))