def party_test():
    fruits_garden =["apple", "oranges", "mangoes"]
    for i in fruits_garden:
        print(i)
    print("\n")
    for num in range(0, 11):
        fruits_garden.append(num)
        print(num)
    print(list(fruits_garden))

party_test()