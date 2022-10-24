# Variable for the int types of people
types_of_people = 11
# Variable for the string "There are ten types of people"
x = f"There are {types_of_people} types of people."

#Variable for the string binary
binary = 'binary'
#Variable for the string do_not
do_not = "don't"
#variable for the string "Those who know binary and those who don't"
y = f"Those who know {binary} and those who {do_not}."

#Prints variable x contents
print(x)
# Prints variable y contents
print

# Used the format string to print strings and content of x
print(f"I said: {x}")
# Used the format string to print some strings and contents of y
print(f"I also said: '{y}")

#Defined variable Hilarious
hilarious = True
# Define a variable to evaluate a joke
joke_evaluation = "Isn't that joke so funny?! {}"

#Print the joke evaluation above using the code below
print(joke_evaluation.format(hilarious))

# Define a string variable for one part of a sentence
w = "This is the left side of..."
# Define a string variable for the other part of a sentence
e = "a string with a right side."

# Concatenate or add both variables together to make a complete sentence 
print(w, e)