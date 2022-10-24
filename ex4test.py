# Variable definition
cars = 100
Space_in_a_Car = 4.0
drivers_driving_cars = 30
passengers = 90

# Cars not driven
cars_not_driven = cars - drivers_driving_cars


# Cars driven
cars_driven = drivers_driving_cars

# carpool capacity
total_carpool_capacity = cars_driven * drivers_driving_cars

#Average person per car
average_person_per_car = passengers / drivers_driving_cars

print ("Cars driven:", cars_driven)
print ("total car pol cap:", total_carpool_capacity)
print ("average car per person:", average_person_per_car)