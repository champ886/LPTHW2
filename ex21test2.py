## Define function

def addition(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Substracting {a} - {b}..")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} - {b}....")
    return a * b

def divide(a, b):
    print(f"Dividing {a} with {b}..")
    return int(a / b)

math1 = addition(5, 6)
math2 = subtract(7, 3)
math3 = multiply(7, 7)
math4 = divide(100, 50)

print(f"math1 = {math1}, math2 = {math2}, math3 = {math3}", f"math4 =", math4)
print(math1 + math2 + math3 + math4)

