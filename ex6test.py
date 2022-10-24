types_of_people = 10
x= f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those people who know {binary}  and those who {do_not}"

print(x)
print(y)

print (f"If I said {x}")
print (f"I also said {y}")

hillarious = False
hillarious_maybe = "Don't Know"
joke_evaluation = "isn't that joke so funny? {}"

print(joke_evaluation.format(hillarious))
print( joke_evaluation.format(hillarious_maybe))

a = joke_evaluation.format(hillarious_maybe)
b= joke_evaluation.format(hillarious)

w = "This is the left side"
e = " A string with a right side"

print (w + e)
print ("\n")
print(a)
print (b)
print ("isn't that joke so funny? {}" .format(hillarious_maybe))