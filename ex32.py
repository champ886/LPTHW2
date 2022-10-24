the_count = [1,2,3,45]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
#For loop says, go through the list and print out 
# each item till the end of the list
for number in the_count:
    print(">>> number =", number)
    print(">>> the_count =", the_count)
    print(f"This is count {number}")

#Same as above
#For loop Fruit says:
#Go through the Fruits list and print out each item till the end of the list
for fruit in fruits:
    print(">>> fruit =", fruit)
    print(">>> fruits =", fruits)
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
#notice we have to use {} since we do not what's in it
#Go through the list "change" and print out each item till the end of the list
for i in change:
    print(">>> i =", i)
    print(">>> change =", change)
    print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 10):
    print(">>> i =", i)
    print(">>> range =", range)
    
    print(f"Adding {i} to the list.")
    print(">>> i =", i)
    #append is a function that lists understand
    elements.append(i)
    
print(">>> elemnts =", elements)
print(">>> after range i =", i)

#now we can print them out too
#For loop says ==> Go through the list and print out each item till the end of list
for i in elements:
    print(f"Element was:  {i}")