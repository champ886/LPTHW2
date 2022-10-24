from pprint import pprint
ten_things = "apples oranges car watch bible quran phone"

print("Wait, there are not ten things on that list...")
print("Let's fix that")
print("." * 50)
print(f"Let's convert these items: '{ten_things}' to a list, first" )

stuff = ten_things.split(" ")
print(">>> ten_thing.splt ", stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee",
            "keyboard", "mouse", "board", "Tissue"]

while len(stuff) != 10:
    print(">>> more_stuff ", more_stuff, "len(more_stuff) ", len(more_stuff))
    pprint(more_stuff)
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")

print("There we go:", stuff)
print(f"We have left over stuff left in list more_stuff: {more_stuff} ")

print("Let's do some stuff with more stuff")


print(stuff[0])
print(stuff[1])
print(stuff[8])
print(stuff[-1])
print(stuff.pop())
print("  ".join(stuff))
print("#".join(stuff[3:5]))
print(" jojo ".join(stuff[6:8])) 
print(stuff)
print(stuff[9])
