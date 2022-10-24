# Introductory statement to condition of code
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

# Code for accepting a door input
door = (input("> "))
print(">>> door input =", door)


#If statement for door option 1
if door == "1":
    print(">>> door =", door)
    #Action ==> for if statement above: prints instrcutions "1" and "2"
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    #1st cascade.. 
    #Code cascades for input above:
    # code  for accepting input above for bear
    bear = input("> ")
    print(">>> Bear input =", bear)

    #if statement for "bear" variable fpor instructions above 
    # option 1
    if bear == "1":
        print(">>> bear =", bear)
        #Action ==> Print actions/more instructions
        print("You have chosen to take the cake.. ", end = " ")
        print ("Choose any of the options below to proceed")
        print("1. The bear eats your face off. Good Job!")
        print("2. the bear licks u and say hi")
        print("3. The bear dances, and farts on its way out")

        bear_reaction = input("> ")

        if bear_reaction == "1":
            print("oh, oh face is off dude..!!")
        elif bear_reaction == "2":
            print("Awwwwwwww!!!")
        elif bear_reaction == "3":
            print("Dance Skelewu")
        else:
            print("Bear complains that you can't play..sobs")

    #Else-if statement for bear option 2
    elif bear == "2":
        print(">>> bear =", bear)
        #Action ==> Print actions/more instructions
        print("You have slected option 2...", end =" ")
        print("Choose any of the options below to proceed")
        print("1. The bear eats your leg off. Good job!")
        print("2. Bear licks your legs and wags its tail..")
        print("3. Bear stands one feat and retreat.")

        bear_reaction02 = int(input("> "))

        if bear_reaction02 == 1:
            print(">>> bear_reaction02 = ", bear_reaction02)
            print("Ha! Legs' off!!!")
        elif bear_reaction02 == 2:
            print("Ha!.. legs wet!!")
        elif bear_reaction02 == 3:
            print("As in.. what the heck?")
        else:
            print(f"looks ur {bear_reaction02} technique worked")
            print("bear scampered!!")
    #Else statement for bear any other option but 1 or 2 above
    # Or if 1/2 above is false.
    else:
        #Action==> Prints actions/ more instructions
        print(f"Well doing {bear} is probably better.")
        print("Bear runs away")

#If Statement for door option 2
elif door == "2":
    print(">>> door input =", door)
    #Action ==> Print instructions 1,2,and 3 below:
    print("You stare into the endless abyss of Cthulhu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies")

    #1st -- Cascade....
    #Input for insanity (Intruction 1,2,3 above)
    insanity = input("> ")
    print(">>> door 2 insanity =", insanity)

    #First if statement for Insanity variable for above 1 or 2
    if insanity == "1" or insanity == "2":
        #Action ==> prints action / more instructions
        print(">>> Door 2 survives branch")
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
        print("Here, are options of what you could do next:....")
        print("1. Choose 1 to power your mind and ", end = " ")
        print("and live of jello forever")
        print("2. Chosse 2 to appeal to cthulu for more time to get ", end =" ")
        print(" used to Jello power")
        print("3. choose 3. to shutdown jello power and use akamu", end =" ")
        print(" as a sub in the meantime")

        insanity_reaction = input("> ")

        if insanity_reaction == "1":
            print("Welcome to Jello power!!")
            print("How do you feel?")
            print(" 1. Type 'relief' if u are happy")
            print(" 2. Type 'sad' if u are sad")
            

            feelings = input("> ")

            if feelings == "relief" or feelings == "Relief":
                print("Well, u had better be!")
            elif feelings == "Sad" or feelings =="sad":
                print("Deal with it!")
            else:
                print("U are right, ur feelings do not matter")
        elif insanity_reaction == "2":
            print("Awaiting Cthulu's approval")
        elif insanity_reaction == "3":
            print("Akamu is activated..dawg!!")
        else:
            print("You are stuck with Jello forever..", end =" ")
            print("Good luck!")

    else:
        #Action ==> prints action / more instructions
        print("Door 2 rots branch.")
        print("The insanity rots your eyes into a pool of muck")
        print("Good job!")

#Else statement for Door (Main If Statement).. 
# That is , if not door 1 or door2
else:
    #Action ==> print action / more instruction below:
    print("You stumble and fall on a knife and die.. Good job!")
