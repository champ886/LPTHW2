
from pprint import pprint
#ten_things variable contains or is assigned a set of string characters
ten_things = "Apples Oranges Crows Telephone Light Sugar"

#print to say that htere aren't ten things on that list
print("Wait there are not 10 things in that list. Let's fix that.")

#Assign variable stuff to "ten_things.split(' ') 
# ==>Which also means making ten_things a list by adding the .split(' ")" 
#Assign variable stuff ten_things.split(' ')
stuff = ten_things.split(' ')
print(">>> ten_thing.splt ", stuff)
#Creating another list more stuff to
#remove items from to add list "stuff", which ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "corn", "Banana", "Girl", "Boy"]

#Use while statement to match condition that 10 things need to be in the list..
#  .. or  the length of stuff list "len(stuff)"" needs to be 10 
while len(stuff) <= 10:
    print(">>> more_stuff ", more_stuff, "len(more_stuff) ", len(more_stuff))
    pprint(more_stuff)
    #Assign variable "next_one" to "more_stuff.pop()"
    next_one = more_stuff.pop() #Call ==> pop on more_stuff
    print("Adding: ", next_one)
    #Append variable next_one to stuff
    stuff.append(next_one)
    #Print a summary statement
    print(f"There are {len(stuff)} items now.")

#prints list stuff
print("There we go: ", stuff)

#playing around with list stuff
print("Let's do some things with stuff.")

#print item in postion 1
print(stuff[1])
print(stuff[-1]) #Whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) #what? cool!
print("#".join(stuff[3:5])) # super stellar!
