
#Defining the "cheese_and_crackers" function using cheese_count parameters and
#  boxes_of_crackers parameters too
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #Action the function needs to take, 
    # firstly print chese count by calling cheese_count function
    print(">>> cheese_count=", cheese_count, "boxes_of_crackers=", boxes_of_crackers)
    print(f"You have {cheese_count} cheeses!")
    # secondly, print boxes of crackers by calling boxes_of_crackers function
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #Random string/text to display
    print("Man that's enough for a party!")
    #Random as well
    print("Get a blanket.\n")
    print("<<< exit cheese_and_crackers")

#giving the function arguments DIRECTLY in 2 
# parameters: cheese count and crackers
print("We can just give the function numbers directly:")
#20 ==> argument cheese_count
#30 ==> boxes_of_crackers
cheese_and_crackers(20, 30)


#Or just using variables random variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

#Substituting the variables above to the postions below 
# for cheese_count and boxes_of_crackersparameters defined in function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#using maths to directly pass arguments to the function
print("We can even do math inside too:")
# 10 + 20 = cheese
#5 + 6 = crackers
cheese_and_crackers(10+20, 5+6)


#combining variables and math using the + sign to =
#  pass arguments to  cheese and crackers parameters
print("And we can combine the two, variables and math:")

#Amount of cheese + 100 = cheese
#amount of crackers + 1000 = crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

ten =10
twelve =12
cheese_and_crackers(ten, twelve)

cheese_and_crackers(amount_of_crackers, amount_of_cheese)