def start():
    from sys import argv
    myScript, name = argv
    print("***ENTER THE GARDEN OF LIFE***")
    name = input("Please enter your name: ")
    print(f"""Hi {name}
    ++++++ Welcome to the Garden of Life+++++++")
    {name}, you now  have 2 paths to take, choose 1:
    Type 'narrow' to choose to the narrow path
    Type 'broad' to choose the broad path""")

    choice = input("> ")

    if choice == "narrow" or choice == "Narrow" or choice == "NARROW":
        print("Welcome to the narrow path leading to life")
        narrow_path_choice()

    elif "broad" in choice or "Broad" in choice or "Broad" in choice:
        print("Welcome to the broad way leading to destruction")
        broad_path_choice()

    else:
        print ("You can't play this gane called life... Goodbye")
        exit(0)

def narrow_path_choice():
    print("Choose 'fight' to continue")
    print("Choose 'run' to quit")

    choice = input("> ")

    if choice =="fight":
        print("""You are now in narrow
        Make a chocie as to how to proceed""")
        narrow_path_fight()

    elif "run" in choice:
        print("You have to make a choice to play")
        start()
    else:
        print("not an option !")
        start()

def choices():
    snakes_fight = False
    lions_fight = False
    sharks_fight = False
    food_rest = False
    run = False
    person_endure = True
    person_fight = False
    give_up = False


def narrow_path_fight():
    print("This path is difficult")
    print("You need to choose from the challenges below")
    print("To win the prize")
    print("Avoid snakes: 'snakes'")
    print("Fight Lions: 'lions'")
    print("Defeat sharks: 'sharks'")
    print("Ejoy some food: 'food'")
    print("Run a marathon: 'run'")
    snakes_fight = False
    lions_fight = False
    sharks_fight = False
    food_rest = False
    run = False
    person_endure = True
    person_fight = False
    give_up = False

    while True:

        choice_1 = input("> ")

        if choice_1 == "snakes" and person_endure:
            print("Avoiding Snakes")
            print("On to the next challenge")
            snakes_fight = True
        
        elif choice_1 == "lions" and snakes_fight and person_endure:
            print("Defeating the lions")
            lions_fight = True
            snakes_fight = True

        elif "sharks" in choice_1 and lions_fight and person_endure and not person_fight and snakes_fight:
           print("Defeating Sharks")
           sharks_fight = True
            
        elif choice_1 == "food": #and sharks_fight:
            print("Enjoy some nourishment")
            fruits()
            food_rest = True

        elif choice_1 == "run": # and food_rest:
            #print("Race Completed!")
            run = True
            race_completed("Race completed")

        else:
            print("You cannot skip any challenge")
            print("You start again")
            print("\n")
            start()

def race_completed(result):
    print(result)
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
            print ("You must be enjoying your party with the islanders while sipping coffee")
            party_choice = True

        elif "snakes" in choice and party_choice:
            print(".... Fighting snakes......")
            print("..........")
            dead("Sorry mate.. You are deader thand dead .. not fit enough")
            
        else:
            start()

def dead(reason):
    print(reason, "you were shortsighted .. goodbye!")
    exit(0)

def fruits():
    print("Choose: 'basket' (fruits already in  basket)")
    print("Choose: 'pick' (Pick from tree)")
    
    choice = input("> ")

    if choice == "basket":
        fruit_options = ["Apples", "Mangoes", "Bananas" ]
        item=0
        for fruit in fruit_options:
            
            item = item + 1
            print(f"You have picked fruit {fruit}")
            print(f"item {item}, {fruit}")

    elif "pick" in choice:
        pick_option = []
        fruit_on_trees = ["Apples", "limes", "corn", "guava", "lemons"]

        for pick in fruit_on_trees:
            pick_option.append(pick)
            print(f"You have picked {pick}")
            print(pick_option)
    else:
        fruits()

        

start()
        