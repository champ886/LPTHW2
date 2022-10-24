people = 20
cats = 30
dogs = 15


if people < cats:
    print(">>> people =", people, "cats =", cats)
    print("Too many cats! The world is doomed!")

if people > cats:
    print(">>> people =", people, "cats =", cats)
    print("Not many cats! The world is saved!")

if people < dogs:
    print(">>> people =", people, "dogs =", dogs)
    print("The world is drooled on!..Yo")

if people > dogs:
    print(">>> people =", people, "dogs =", dogs)
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print(">>> people =", people, "dogs =", dogs)
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print(">>> people =", people, "dogs =", dogs)
    print("People are less than or equal to dogs")

if people == dogs:
    print(">>> people =", people, "dogs =", dogs)
    print("People are dogs.")

    