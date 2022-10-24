#Define variables and list
i = 0
numbers = []

k = 6

#Set a true boolean condition
while i < k:
    print(">>> i =", i)
    print(f"At the top i is {i}")
    print(">>> numbers list =", numbers)
    numbers.append(i)

#Set an incrementer
#incrementer jumps to the next postion on the list till it satisfies its
#true statement above ==> "i < k" or "0 < 6"
    i += 1
    print(">>> 'i' increments = ", i)
    print("Numbers list now: ", numbers)
    print(f"At the bottom i is {i}")
    print("\n")


print("The numbers: ")

for num in numbers:
    print(num)