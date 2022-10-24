def looper(i, k):
    numbers =[]
    for num in range(i, k):
        print(f"At the top num is: {num}")
        
        numbers.append(num)
        
        print("Numbers position in list: ", numbers)

    print("\n")
    print("Total list content: ", numbers)
    #numbers = range(i, k)
    for num in numbers:
        print(f"Number is {num}")
        
    


looper(0, 6)

print("\n")

looper(1, 7)

