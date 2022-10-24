#Defining variables
people = 30
cars = 40
trucks = 15

#if (TRUE) cars are greater than people.. print action in indent
if cars > people:
    print("We should take the cars.")

#Else if (TRUE) cars are lesser than people ... take action in indent  ..PRINT
elif cars < people:
    print("We should not take the cars.")

#Else if (FALSE).. as in not the same as above
#  cars neither greter than people or lesser..
#..take action in indent
else:
    print("We can't decide.")

#if (True) trucks are greater than cars.. take action in indent
if trucks > cars:
    print("There's too many trucks.")
#else if (True) again.. take action in indent.
elif trucks < cars:
    print("Maybe we could take the trucks.")
#Else if (False) as in not same as above if and elif.. take action in indent
else:
    print("We still can't decide.")

#If True (People greate than Trucks)... take action in indent
if people > trucks:
    print("Alright, let's just take the trucks.")
#Else if FALSE(as in not the same as above), take action in indent
else:
    print("Fine, let's stay home then.")