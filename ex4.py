# defines number of cars
cars = 100

# defines how many people can fit in a car
space_in_a_car = 4.0

# defines how many drivers
drivers = 30

# defines how many passengers
passengers = 90

# defines how many cars will not be driven (total number of cars - total number of drivers)
cars_not_driven = cars - drivers

# defines how many cars will be driven (this is driven by how many drivers are available)
cars_driven = drivers

# defines carpool capacity which is found by multiplying the cars available by how many 
#people can fit in each car
carpool_capacity = cars_driven * space_in_a_car

# defines average number of passengers in each car by taking the total number of passengers 
#and dividing that by how many cars will be driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."