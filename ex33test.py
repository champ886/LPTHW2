def looper(i, k, d):
    numbers =[]
    while i < k:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + d
        print(f"At the bottom i is {i}")
        print("Numbers now: ", numbers)

    print(numbers)
    
    for num in numbers:
        print(num)


looper(0, 6, 2)

print("\n")

looper(1, 7, 3)

