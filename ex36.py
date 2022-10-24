
def start():
    from sys import argv
    my_script, name = argv
    print("****ENTER THE  GARDEN OF LIFE****")
    name = input("Please enter your name: ")
    print(f"Hi {name}, ++++++ Welcome to the Garden of Life+++++++")
    print(f"{name}, you now  have 2 paths to take, choose 1:")
    print("Type 'narrow' to choose to the narrow path")
    print("Type 'broad' to choose the broad path")

    choice = input("> ")

    if choice == "narrow":
        print("Welcome to the narrow path leading to life")
        narrow_path_choice()
        
    elif choice == "broad":
        print("Welcome to the broad and spacious road leading to destruction")
        broad_path_choice()

    else:
        print("You cant play this game called life..Goodbye!!")
        exit(0)

def narrow_path_choice():
    print("Choose 'fight' to continue")
    print("Choose 'run' to quit")

    choice = input("> ")
    if choice == "fight":
        print("Welcome to narrow!")
        narrow_path_fight()

    elif choice == "run":
        print("You have to choose and play")
        start()


def narrow_path_fight():
    print("This path is difficult")
    print("You need to choose from the challenges below")
    print("To win the prize")
    print("Avoid snakes: 'snakes'")
    print("Fight Lions: 'lions'")
    print("Defeat sharks: 'sharks'")
    print("Ejoy some food: 'food'")
    print("Run a marathon: 'run'")
    snake_fight = False
    lion_fight = False
    shark_fight = False
    food_rest = False
    run = False
    person_endure = True
    person_fight = True
    give_up = False

    while True:

        choice_1 = input("> ")
        print(">>> choice_1 =", choice_1)
        
        if choice_1 == "snakes" and person_endure:
            print("Avoiding snakes")
            print("onto the next challenge")
            snake_fight = True
            print(">>> snake_fight", snake_fight)
               
        elif choice_1 == "lions" and snake_fight:
            print(">>> choice_1 =", choice_1, "and", snake_fight)
            print("Defeating the the Lions")
            lion_fight = True

        elif choice_1 == "sharks" and lion_fight:
            print("Fighting Sharks")
            shark_fight = True

        elif choice_1 == "food": #and shark_fight:
            print("Enjoying some nourishments")
            fruits()
            food_rest  = True

        elif choice_1 == "run": # and food_rest:
            print("Race completed")
            run = True
            race_completed()


        else:
            print("You cannot skip any challenge!")
            print("You start again!")
            print("\n")
            start()

def race_completed():
    print("You have reach the end!")
    exit(0)

def broad_path_choice():
    print("welcome to the broad path..Enjoy??!")
    print("\n")
    print("Choose from the lists below:")
    print("'coffee': to sip coffee")
    print("'party' to party with the islanders")
    print("'snakes' to avoid snakes")
    print("'lions' to fight lions")
    print("'sharks' to fight sharks")
    print("'run' to marathon it")

    coffee_choice = False
    party_choice = False
    snakes_choice = False
    lions_choice = False
    sharks_choice = False
    run_choice = False

    while True:

        choice = input("> ")

        if choice == "coffee":
            print("Keep sipping")
            coffee_choice = True

        elif choice == "party" and coffee_choice:
            print("U must be enjyoing the party with the islanders!")
            party_choice = True

        elif choice == "snakes" and party_choice:
            print(".... Fighting snakes......")
            print("..........")
            dead("U lost the battle.. not fit enough.")

        else:
            start()
              
def dead(reason):
    print(reason, "U were shortsighted...Goodbye!!")
    exit(0)

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
        fruit_on_trees = ["Apples", "limes", "corn", "guava", "lemons"]
        
        for fruit in fruit_on_trees:
            print("Adding...  ",fruit, " to your basket")
            fruit_pick.append(fruit)
        print(f"You now have  {fruit_pick[0]}, {fruit_pick[1]},", end = " ")
        print(fruit_pick[2],',',fruit_pick[3],'and',fruit_pick[4],',', end = " ")
        print ("in your basket")
        print("You now well nourished")
        print("To finish your race")
        print(fruit_pick)


start()