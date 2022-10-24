#prints the string mary had a little lamb
print("Mary had a little lamb")
#Prints string and adds a .format to add snow to the empty curly braces
print("Its fleece was white as {}.".format('snow')) #or use line below
#print(f"Its fleece was white as {'snow'}.")
#prints more string statement
print("And everywhere that Mary went.")
#prints dots.. ten times
print("." * 10) #What did that do?


#Assigns c to variable end1
end1 = "c"
#Assigns h to variable end2
end2 = "h"
#Assigns e to variable end3
end3 = "e"
#Assigns e to variable end4
end4 = "e"
#Assigns s to variable end5
end5 = "s"
#Assigns s to variable end6
end6 = "e"
#Assigns B  to variable end7
end7 = "B"
#Assigns u to variable end8
end8 = "u"
#Assigns r to variable end9
end9 = "r"
#Assigns g to variable end 10
end10 = "g"
#Assigns e to variable end11
end11 = "e"
#Assigns r to variable end12
end12 = "r"

# Champion added below to check for end usage
Bend1 = "l"
Bend2 = "o"
Bend3 = "o"
Bend4 = "k"

Bend5 = "h"
Bend6 = "e"
Bend7 = "r"
Bend8 = "e"

# watch end = ' ' at the end. try removing it to see what happens
# Concatenates or adds end variabes to make a sentence
#The  single colon (end= ' ') at the allows for the concatenated variables to continue in the same line
#While the empty (space-inbetween)the colons allows for between the two words Cheese below and Burger line 41
print(end1 + end2 + end3 + end4 + end5 + end6, end=': ' )
#Prints Burger based on concatenated variables.
print(end7 + end8 + end9 + end10 + end11 + end12)

# Proves that end is python reserved variable for the function of continuing sentence on the same line
print(Bend1 + Bend2 + Bend3 + Bend4, end= ' ')
print(Bend5 + Bend6 + Bend7 + Bend8)