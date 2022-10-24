#Defining variables
people = 40
cars = 40
trucks = 50

print("if.. cars and people")
#if (TRUE) cars are greater than people.. print action in indent
if cars > people:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("We should take the cars.")

#Else if (TRUE) cars are lesser than people ... take action in indent  ..PRINT
elif cars < people:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("We should not take the cars.")

#Else if (FALSE).. as in not the same as above
#  cars neither greter than people or lesser..
#..take action in indent
# in this case cars == people
elif cars == people:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("We  can't decide")

else:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("We can't decide.")

print("\n")





#++++++++++Trucks+++++++++++++++++++++++++++

print("if truck cars or people")
#if (True) trucks are greater than cars.. take action in indent
if trucks < cars:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("There's too many trucks.")
#else if (True) again.. take action in indent.
elif trucks < cars or people == cars:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("Maybe we could take the trucks.")
#Else if (False) as in not same as above if and elif.. take action in indent
else:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("We still can't decide.")

print("\n")




#+++++++ Trucks and people+++++++

print("if trucks and people only")

#If True (People greate than Trucks)... take action in indent
if people < trucks and cars == people:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("Alright, let's just take the trucks.")
#Else if FALSE(as in not the same as above), take action in indent
else:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("Fine, let's stay home then.")