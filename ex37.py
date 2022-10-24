

with open("ex37text.txt") as k:
    print(k.read())


no_questions = [50,60,70,80,90]

for g in no_questions:
    assert g is not 0
    if g >= 50:
        print("This student passed!")
    else:
        print("This student failed")

print("Program complete")


for letter in 'python':
    if letter == 'h':
        break
    print("Current Letter: ", letter)

var = 1
while var < 10:
    print("Current variable value: ", var)
    var = var + 1
    if var == 5:
        break
    




#++++++++++While loops++++++++++++++++++++++++
#Use a seperate variable for the incrementer
x = 0
# use a seperate variable for the conditional statement
y = 50

while y > 10:#Condition
    print("Value of y: ", y)
    x = x+1 #incrementer/Decrementer
    print("x is", x)
    if x == 15:
        print("Hits '15' and stops looping :", x)
        break
   # elif x <= 14:
   #     print("Continues looping: ", x)
   #     break
    else:
        continue

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

def divide(x, y):
    try:
       #Floor division: Gives only fractional
       # part as answer
       result = x // y
       # print("Yeah : Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry : You are dividing by zero")
    else:
        print("Yeah: Your answer is: ", result)
    finally:
        print("This is always executed", result)
    return x // y

divide(3, 2)
divide(6, 2)

print(divide(3, 2))
print(divide(6, 2))


#+++++ Try and Finally with files ++++++#





def myfunc():
    print("Python is ",  x)


myfunc()


#Testing lambda#

b = lambda a : a + 10
print(b(5))

c= lambda d,e,f : d+e+f
c(5,6,2)

x= lambda y,m,q: y * m // q
print(x(2,3,2))



#++++ Using pass++++
sequence = [3,4,5,6,7]

for val in sequence:
    pass

def myfunc2():
    pass

n = 10

for i in range(n):
    pass
    #print(i)

#+++ Using Raise Keyword+++#

l = 100

#if l > 0:
#    print(">>>", l)
#   raise Exception("Sorry no numbers higher than  zero")

k ="hello"

#if type(k)  is not int:
#    raise TypeError("Only intergers are allowed")


def mytry_test(b, c):
    try:
       a = b * c
        #print("Hey")
        #pass
    except multiplyingByZero:
     
        print("You cannot multiply by zero")
    finally:
    
        print("The result is always ", a)
    return b*c

mytry_test(3,4)
mytry_test(3, 0)
#print(mytry_test(3, 4))

#+++ Using "With" with files and exception++#

file = open('/home/champ/Desktop/Python_Training_LPTHW/testfileEx37.txt')
print(file.read())

file02 = open('/home/champ/Desktop/Python_Training_LPTHW/testfileEx37.txt', 'w')
file02.write("Hello Champ!!")
file02.close()
file02 = open('/home/champ/Desktop/Python_Training_LPTHW/testfileEx37.txt')
print(">>> file02.write", file02)
print(file02.read())

# With try and finally

file = open('/home/champ/Desktop/Python_Training_LPTHW/testfileEx37.txt', 'w')
try:
    file.write("Hello world")
finally:
    file.close()
    file = open('/home/champ/Desktop/Python_Training_LPTHW/testfileEx37.txt')
    print(">>> file02.write", file02)
    print(file.read())

#drumrolls.dmdumdumdum ...Now using With statement
#..simplifies the management of common resoruces like files eg (textfile37.txt)

with open('/home/champ/Desktop/Python_Training_LPTHW/testfileEx37.txt', 'w') as file:
    file.write("Hello Champ \n ...Again")
    file.write("\n...and again")
    print(">>> file", file)

with open ('/home/champ/Desktop/Python_Training_LPTHW/testfileEx3702.txt', 'w') as file:
    file.write("Yo my man!!")
with open('/home/champ/Desktop/Python_Training_LPTHW/testfileEx3702.txt') as file:
    print(file.read())

#.... Using Yield......
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

def testyield():
    yield "We are all capable achieving our potential"
    yield "..Yet many fall short"

output = testyield()
print(output)

for k in output:
    print(k)


