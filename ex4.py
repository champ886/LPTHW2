# Variable definition: Total number of cars
cars = 100

#Variable definition: How much can a car fit?
space_in_a_car = 4.0
#space_in_a_car = 4

#Variable definition: How many drivers?
drivers = 30

#Variable definition: What are the total number of passengers
passengers = 90

#Variable definition: How many cars are not being driven?
cars_not_driven = cars - drivers

#Variable definition: How many cars are driven?
cars_driven = drivers

#Variable definition: What is the collective number of carpool capacity in all cars?
carpool_capacity = cars_driven * space_in_a_car

#Variable definition: Average Passenegrs per car?
average_passengers_per_car = passengers / cars_driven




#using variables above for below:

#How many cars are available?
print("There are ", cars, "cars available.")

#How many Drivers are available?
print("There are only", drivers, "drivers available.")

#How many cars are yet to be driven?
print("There will be", cars_not_driven, "empty cars today.")

#What are the total number of  passengers that can be transported or carpooled  (in all cars) today?
print("We can transport", carpool_capacity, "people today.")

#How many passengers are available for carpooling today?
print("We have", passengers, "to carpool today.")

#How many passengers can fit in one car?
print("We need to think about", average_passengers_per_car, "in each car.")