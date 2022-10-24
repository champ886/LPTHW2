from pprint import pprint

twelve_things = "Yams lemon beans bacon cashew plum sugar oregano"

print(f"list {twelve_things}, not up to 12 things")
print("Let's work on that")

stuff = twelve_things.split(' ')
print(">>> stuff ", stuff)
more_things = " gym crossfit workout core strength flexibility endurance"
more_stuff = more_things.split(' ')
print(">>> more_stuff", more_stuff)


while len(stuff) != 12:
    print("Removing stuff from more_stuff")
    next_one = more_stuff.pop()
    print(">>> next_one ", next_one)
    print(">>> more_stuff ", more_stuff, len(more_stuff))
    print("adding more items to stuff: ")
    stuff.append(next_one)
    print(stuff)
print(stuff)

print(f"There are now {len(stuff)} items in the 'stuff' list")

#prints first item in list
print(stuff[0])
#Prints last item in list
print(stuff[-1])
#Prints item in position 6, Item 7
print(stuff[6])
#prints first item from list
print(stuff.pop(0))
pprint(stuff)
#prints last item in list as above, but pops/takes off the list
print(stuff.pop(-1))
pprint(stuff)
#print last item with pop proof
print(stuff.pop(-1))
print(stuff)
#using join
print("  ".join(stuff))
print(" and ".join(stuff[3:5]))
#print(stuff)