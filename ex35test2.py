

def sale(royal_gala):
    print(royal_gala,", Are they  on sale?")
    print('if on sale press "Yes"')
    print('if not "no"')

    sale_option = input("> ")

    if sale_option == "yes":
        print("buy 12!")
        exit(0)
    elif sale_option == "no":
        print("buy 1")
    else:
        print("not interested")


def begin():
    print("Do you like apples?")
    print("Type 'lala' if you do")
    print("or type 'royal gala' if you just love those")
    love_apples =True


    while True:
        option = input("> ")

        if option == "lala" and love_apples:
            print("Yeah baby!!")

        elif option == "royal gala" or option == love_apples:
            print("Make sure they are on sale!.. Enjoy!")
            sale("sale option")

        else:
            print("Type properly")

begin()


