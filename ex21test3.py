def add(a, b):
    print(f"adding {a} + {b}")
    return a + b

def subtract (a, b):
    print(f"Subtracting {a} from {b}")
    return a - b

def multiply(a, b):
    print (f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b}")
    a = 40
    #divideme =a * b
    return a / b


print("Doing some math with the above functions")

age =add(3,5)
print(age)

height = subtract(92, 6)
print(height)

weight = multiply(50, 6)
print(weight)

iq = divide(400, 2)
print(iq)

print(f"""So you are {age} years old, {height} cm tall, 
weigh {weight} kilos and have an IQ of {iq}""")

print("\n")
print("Total from above")
print(age + weight + height + iq)

functions_in_one = add(age, subtract(height, multiply(weight, divide (iq, 1))))

print(f"That becomes {functions_in_one}")