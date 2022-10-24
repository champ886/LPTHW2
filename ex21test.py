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



math1 = divide(34, 100)
math2 = add(24, math1)
math3 = subtract(math2, 1023)


print(f"math1: {math1} math2: {math2} math3:", math3)

formula = subtract(math2, 1023)

print(f"{formula}")