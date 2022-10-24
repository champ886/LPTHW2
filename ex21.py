#defining function "add"
def add(a, b):
    print(">>> add: a=", a, "add: b=", b )
    #Action ==> printing statement adding values of a and b
    print(f"ADDING {a} + {b}")
    #Action ==> Return the values or the result of the values a and b to function
    return a + b
    print("<<< exit add")


#definifn function subtract
def subtract(a, b):
    #Action ==> Print subtracting a from b
    print(f"SUBTRACTING {a} - {b}")
    #Action return values of result of a -b
    return a - b


#defining function multiply
def multiply(a, b):
    print(f"MULTIPLYING  {a} * {b}")
    #Action ==> return as above
    return a * b


#Defining function divide
def divide(a, b):
    #Action ==> As above
    print(f"DIVIDING {a} / {b}")
    #Action ==> As above
    return a / b

print("\n")

######## Using functions starts from below ########################



print("Let's do some math with just fractions!")



#Assigning variables to function "age" and calling the function
age = add(30, 5)
print(">>> age=", repr(age))
#Assigning variable height to function "Subtract" and calling the function
height = subtract(78, 4)
print(">>> height=", height)
#Assigning variable weight to function "multiply" and calling the function
weight = multiply(90, 2)
print(">>> weight=", weight)
#Assigining variable "iq" to function "divide" and calling the function
iq = divide(100, 2)


print("\n")
print("\n")

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("\n")

#A puzzle for the extra credit, type it anyway
print("Here is the puzzle")

print (age + weight + height + iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print(
    ">>> what =", what, repr(what), "age=", repr(age), 
    "subtract=", repr(subtract), "height=", height,
    "multiply=", multiply, "weight =", weight,
    "divide=", divide
)

print("That becomes: ", what, "Can you do it by hand?")