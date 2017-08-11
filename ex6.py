# tells how many types of people there are and calls it x
x = "There are %d types of people." % 10

# defines binary and do_not as words
binary = "binary"
do_not = "don't"

# defines y as a statement about types of people
y = "Those who know %s and those who %s." % (binary, do_not)

# prints a message of number and types of people
print x
print y

# prints x with another message before it
print "I said: %r." % x

# prints y with another message before it
print "I also said: '%s'." % y

# defines hilarious as not true
hilarious = False

# prompts the use to consider if the joke is funny...it's not
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# defines strings for the variables w and e
w = "This is the left side of..."
e = "a string with a right side."

# prints a message of w and e
print w + e