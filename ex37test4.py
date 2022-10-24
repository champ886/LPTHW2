with open("ex37text.txt") as k:
    print(k.read())

b = open("ex37text.txt")
print(b.read())

no_questions = [50,60,70,80,80]

for g in no_questions:
   # assert g is not 0
    if g>= 50:
        print(g)
        print("This student passed!!")
    else:
        print("This student failed")

print("Program completed!")

for letter in 'Champion':
    if letter == "n":
        print(letter == "a")
        break
    print(f"Current letter is ...{letter}")

var = 1
while var < 10:
    print("Current variable is ...", var)
    var = var + 1
    if var == 5:
        break


x =0
y = 60

while y > 10:
    print ("Value of y: ", y)
    x = x + 1
    print ("Vlaue of x: ", x)

    if x == 13:
        print("Hits 15 and stops looping:", x)
        
    elif x == 15:
        print("Hits 13 and stops looping:", x)
    elif x == 25:
        print("Hits 15 and stops looping:", x)
        break    
    else:
        continue

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Sorry you are dividing by zero")
    else:
        print("Yea, your answer is :", result)
    finally:
        print("Tis is always executed: ", result)
    return x // y

print(divide(3, 2))
print(divide(6, 2))
#print(divide(3, 0))


# testing global variable x ###

def myGlobalVar():
    print("Global variable is: ", x)

myGlobalVar()

#Testing Lambda

c = lambda z, c: z * c
print(c(1, 2))

b = lambda d,e,f: d * e * f
print(b(4,5,6))


#++++ Using pass++++
sequence = [3,4,5,6,7]

for val in sequence:
    pass
def myfunc2():
    pass
n = 10

for i in range(n):
    pass


l = 100


file_open = open('/home/champ/Desktop/Python_Training_LPTHW/ex37text.txt')
print(file_open.read())

file_open = open('/home/champ/Desktop/Python_Training_LPTHW/ex37text.txt', "a")
file_open.write("\nYea.. Champ!\n Going good Mayte!!!\n Goood Maytee!")

file_open = open('/home/champ/Desktop/Python_Training_LPTHW/ex37text.txt')

print(file_open.read())

# Using with and try

file_open02 = open('/home/champ/Desktop/Python_Training_LPTHW/ex37text.txt', "w")
try:
    file_open02.write("Hellow World")
finally:
    file_open02.close()
    file_open02 = open('/home/champ/Desktop/Python_Training_LPTHW/ex37text.txt')
    print(file_open02.read())

#file01= open('/home/champ/Desktop/Python_Training_LPTHW/ex37text.txt')
with open('/home/champ/Desktop/Python_Training_LPTHW/ex37text.txt', "w") as file01:
    file01.write("Hello Champ again")
    file01.write("\n... and again")
    file01.write("\n...and again")
with open('/home/champ/Desktop/Python_Training_LPTHW/ex37text.txt') as file01:
    print(file01.read())

def simple_generator():
        d = 1
        yield d
        yield d + 1
        yield d + 2

print(simple_generator)
generator_object = simple_generator()
print(generator_object)

for i in generator_object:
    print(i)



