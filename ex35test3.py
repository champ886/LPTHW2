from sys import exit

def gold_room():
    print("THis room is full of glod. How much do ou take?")
    choice = input("> ")

    if choice == 1 or "0" in choice:
        how_much = int(choice)
    else:
        dead("Man, leanr to type a number!!")

    if how_much < 50:
        print("Nice, you are not greedy...you win")
        exit(0)
    else:
        print("You greedy bastard!")

def bear_room():
    print("""Theere is a bear here,
    and it has a lot of honey..
    The fat bear is in front of another door.
    How are you gonna get past it??""")

    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you, and then slaps your face off! ")
        elif choice == "taunt bear" and not bear_moved:
            print('choice == "taunt bear" and not bear_moved>>>', choice == "taunt bear" and not bear_moved)
            print("""You are a brave man/guy/girl"
            The bear has moved from the door 
            You can now go through the door""")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead ("The bear gets angery and chews ur arm off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have got no idea what that means!!")

def Cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it , whatever stares at you and you go insane.")
    print("Do you flee for your life or you eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif choice == "head":
        dead("Well, that was tasty")
    else:
        Cthulhu_room()


def dead(why):
    print(why, "Good Job")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and to your left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left" or "Left" or "LEFT":
        bear_room()
    elif "right" or "Right" or "RIGHT" in choice:
        Cthulhu_room()
    else:
        dead("You stumble across the room until you starve and die...dead")

start()
