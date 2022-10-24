def start():
    print("You are in a dark room.")
    print("There is a door to your right and left")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("Your choices are: ")
    print("'take honey'")
    print("'tail', to touch bears tail")
    print("'dance' to dance with bear")
    print("'open door' to open door")
    #Bear is not moving by default
    bear_moved = False
    print(">>> bear_moved =", bear_moved)

    #Keeps looping through the conditions till it encounters another true statement
    while True == True:
        
        choice = input("> ")
        print(">>> choice =", choice)

        print("\n")
        if choice == "take honey":
            print(">>> choice =", choice)
            dead("The bear looks at you then slaps your face off.")


        #Boolean result of "choice" = True (taunt bear) and True.. 
        # bear_moved = False
        # notFalse = True
        # Therefore "not bear_moved" = True
        # Then Boolean choice ==  True and True
        # Remember only when the condition is true does the code run
        # If false it skips it and goes to else condition
        # 
        #     OR
        # 
        # If True in the case of the loop above,
        # It loops to the next condition
        # Or Executes a function and exit loop and condition   
        elif choice == "taunt bear" or choice == bear_moved:
            print(">>> choice =", choice)
            print(">>> bear_moved =", bear_moved)
            #print(">>> bear_moved =", bear_moved)
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        #At this point elif above will keep looping unless it branches of to the next
        # condition (True Statement) or encounter an exit function.
        elif "tail" in choice:
            tail_hold()
        elif choice == "dance" or choice == bear_moved:
            print("You are dancing with daddy bear")
            print("Now you can open the door")
            bear_moved = True
        elif choice == "open door" and bear_moved:
            print("bear_moved =", bear_moved)
            print("Aha.. Bien venido!")
            #dead("Dead mate!")
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    print ("Or do you look for an invisible tail")

    choice = input("> ")
    print(">>> choice ==", choice)

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    elif "tail" in choice:
        invisible_tail()
    
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = int(input("> "))
    print(">>> choice =", choice)

    if choice <= 50:
        #if "0" in choice or "1" in choice:
        how_much = choice
        #   print(">>> how_much =", how_much)
        #print("nice", choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you are not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def tail_hold():
    print("Oh, why did you have to do that?")
    print("Hands off!!")
    exit(0)

def invisible_tail():
    print("You are done mate..dead.. u are")
    dead("I always knew I had one")

start()