the_count = [1,2,3,4,5]
fruits = ["apples", "grapes", "pears", "bananas"]
change = [1, "pennies", 2, "dimes", 3, "quaters"]

for number in the_count:
    print(">>>", the_count)
    print(f"This is count {number}")

for fruit in fruits:
    print(">>>", fruits)
    print(f"A fruit of type: {fruit}")

for i in change:
   # print(">>>", change)
    print(f"You have {i}")

elements = []

for i in range (0, 10):
    print(">>>", i)
    elements.append(i)
    print(elements)

print(elements)

for i in elements:
    print(f"The number is: {i}")