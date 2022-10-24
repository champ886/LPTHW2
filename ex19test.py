def gym_routine (squats, pull_ups):
    print(">>> squats=", squats, "pull_ups=", pull_ups)
    print(f"you did {squats} squat exercises")
    print(f"you did {pull_ups} pull_ups exercises today")
    print("You have done well man")
    print("Puff..!!\n")
    print("<<< exit gym_routine")


#Using variables
amount_of_squats = 10
amount_of_pullups = 50
gym_routine(amount_of_squats, amount_of_pullups)



#using numbers
gym_routine(500, 30)



#using maths
gym_routine(4+50, 70-9)

#using variables + maths
gym_routine(amount_of_squats + 45, amount_of_pullups + 9)

#using strings
gym_routine("twenty", "five hundred")

#
print(f"My gym routine is {gym_routine}")
