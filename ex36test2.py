def fruits():

    print("Choose: 'basket' (fruits already in  basket)")
    print("Choose: 'Pick' (Pick from tree)")

    choice = input("> ")

    if choice == "basket":
        
        fruit_options = ["Apple", "Mangoes", "Oranges"]
        item = 0
        for i in fruit_options:
            item += 1
            print(f"item {item} is {i}")

    elif choice == "pick":
        fruit_pick = []
        fruit_on_trees = ["Apples", "limes", "corn", "guava", "lemon"]
        position = 0
        
        for fruit in fruit_on_trees:
            print(fruit)
            fruit_pick.append(fruit)
        print(fruit_pick)
fruits()