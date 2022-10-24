print(""" You enter a dark room with 2 doors.
Do you go through door#1 or door #2?""")

door = int(input("> "))

if door == 1:
    print ("There is a giant bear here eating a cheesecake")
    print (" What do you do?")
    print ("1. Take the cake ?")
    print ("2. Scream at the bear")

    bear = input("> ")

    if bear == 1:
        print("The bear eats your face off")
    elif bear == 2:
        print("The bear eats your leg off")
    else:
        print (f"Well doing {bear}, is probably better")
        print("Bear runs away")

elif door == 2:
    print("You stare into an endless habit of Cthulus Retina")
    print("Select one of these options ?")
    print("1. Blueberries")
    print("2. Yellow Jacket clothes spins")
    print("3. Understanding revolvers, yelling melodies")

    insanity_choice = input("> ")

    if insanity_choice == 1 or insanity_choice == 2:
        print("Your body survices powered by a mind jello")
    else:
        print("The insanity rots your eyes into a pool of mucky muck")

else:
    print("You stumble ... fall on a knife and die")



