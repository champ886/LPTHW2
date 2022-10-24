from pprint import pprint
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
print(">>> ten_thing.splt ", stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    print(">>> more_stuff ", more_stuff, "len(more_stuff) ", len(more_stuff))
    pprint(more_stuff)
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[0])
print(stuff[1])
print(stuff[8])
print(stuff[-1]) #Whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) #what? cool!
print("#".join(stuff[3:5])) # super stellar!
