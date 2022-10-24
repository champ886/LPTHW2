#Game on
print("You walk in to a forest with 3 pathways")
print("Choose path #1 , #2, or #3")

path = input("> ")

if path == "1":
    print("There dragons are awaiting you")
    print("Choose '1' to dance with the dragon")
    print("Choose '2' to show her ur biceps")

    dragon = input("> ")
    if dragon == "1":
        print("They dance pretty fast.. you lose")
    elif dragon == "2":
        print("She has seen bigger ones.. you win")
    else:
        print("You Die!!")


elif path == "2":
    print("There snakes waiting to Totori your sploicket")
    print("Choose '1' to smash their heads with club")
    print("Choose '2' to  sommersault all the way on that path")
    
    snakes = input("> ")
    if snakes == "1":
        print("Good going.. you win!")
    elif snakes == "2":
        print("Snakes catches you ankle on your 3rd flip!")
        print("You need medics ASAP!")
    else:
        print("You die!!")

elif path == "3":
    print("This is the cramped and Narrow leading to life")
    print("Few are the ones going through it")
    print("Choose 1 to know more about God")
    print("Choose 2 ask a bible student a question")

    cramped = input("> ")

    if cramped == "1":
        print("You will live forever!")
    elif cramped == "2":
        print("You have started well")
    else:
        print("You will die")

else:
    print("You lose!")
    print("Life is about making choices")

