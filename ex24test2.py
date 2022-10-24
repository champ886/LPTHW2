print("let's practice everything")
print("You\'d need to know \'bout escapes with\\ that do:")
print("\n newlines and \t tabs")

poem = ("""
\t The lovely word with logic
\t\tcannot fully understand Bash shells with emotions
\n\t""")

print(poem)

def secretformulaRecipee(started):
    rice_cups = started * 500
    pot_water = rice_cups/2
    chopped_carrots = pot_water + 555
    print("rice:",rice_cups,
     'pot_water:' ,pot_water,
      'carrots:', chopped_carrots)
    return rice_cups, pot_water, chopped_carrots
    

print("Start point at 500")
start_point = 500

#rice_cups = secretformulaRecipee(start_point)
#pot_water = secretformulaRecipee(start_point)
rice_cups, pot_water, chopped_carrots = secretformulaRecipee(start_point)

print("With a starting point of {}".format(start_point))
print (f"The above is the sanme as {start_point}")
print( "or the same as ", start_point)
print("\n")
print ("*" * 50)

print("Start point divided by 10")
start_point = start_point / 10

formula = secretformulaRecipee(start_point)
print("\n")

print("We'd have  in list format ==> {} rice, {} water and {} carrots".format(*formula))

print (f" We'd have {rice_cups}, {pot_water} and {chopped_carrots}")