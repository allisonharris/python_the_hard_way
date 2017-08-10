name = 'Zed A. Shaw'
age = 35 #not a lie
height_inches = 74 # inches
height_centimeters = height_inches * 2.54
weight_pounds = 180 # lbs
weight_kilograms = weight_pounds * 0.453592
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "Let's talk about %s." % name
print "He's %d inches tall and %d centimeters tall." % (height_inches, height_centimeters)
print "He's %d pounds heavy and %d kilograms heavy." % (weight_pounds, weight_kilograms)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


print "If I add %d, %d, and %d I get %d." % (
	age, height_inches, weight_pounds, age + height_inches + weight_pounds)