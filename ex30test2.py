people = 40
cars = 40
trucks = 50

print("If cars... and people")

if cars > people:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("We should take the cars")

elif cars < people:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print("We should not take the cars")

elif cars == people:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print("We can't decide")
    
else:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print("We can't decide")

print("+" * 50)

print("If... trucks and people only")

if trucks > people:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("We are driving the trucks")

elif trucks < people:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print("nope, we can't take the trucks")

elif trucks == people:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print("We can't decide")

else:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print("we can't decide")

print("\n")
print("*" * 50)

print("Truck, cars and people")
trucks = trucks - 10

if trucks > cars and cars == people:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print (" you can take the cars and trucks")

elif trucks > cars and cars == people:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print("Take ONLY 2 cars and all trucks ")

elif trucks < people and cars < people:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print ("There are no vehicles to drive/take")

elif trucks < people or cars < people:
     print(">>> trucks =", trucks, "cars =", cars, "People =", people)
     print("U can choose either cars or trucks")

elif trucks == cars and trucks == people:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("Free for all!")
else:
    print(">>> trucks =", trucks, "cars =", cars, "People =", people)
    print("We cannot decide")
