# create a function to print out the information on cheese and crackers with follow
# up text about a party and blanket
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# assigns amount of cheese and crackers in parenthesis
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# assigns amount of cheese and crackers on individual lines
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# combines above into statement...this is much less efficient than the first way
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# assigns amount of cheese and crackers by adding values
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# assigns amount by combining names and adding values
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)