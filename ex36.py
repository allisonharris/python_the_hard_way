print("Welcome to Jeopard!")
print "1. Social Studies"
print "2. Nutrition"
print "3. Animals"
print "4. Sports"
print "5. Movies"
 
category = raw_input("Select a number to begin: ")
 
if category == "1":
    print("Which fictional city is the home of Batman")
    answer = raw_input("Your answer: ")
    if answer == "Gotham City":
        print "You got it!"
    else:
        print "Nope! Remember to capitalize cities. Game over."

if category == "2":
    print("Spinach is high in which mineral?")
    answer = raw_input("Your answer: ")
    if answer == "iron":
        print "You got it!"
    else:
        print "Nope! Game over."

if category == "3":
    print("Which type of dog has breeds called Scottish, Welsh and Irish?")
    answer = raw_input("Your answer: ")
    if answer == "terrier":
        print "You got it!"
    else:
        print "Nope! Game over."

if category == "4":
    print("Babe Ruth is associated with which sport?")
    answer = raw_input("Your answer: ")
    if answer == "baseball":
        print "You got it!"
    else:
        print "Nope! Game over."

if category == "5":
    print("In the film Babe, what type of animal was Babe?")
    answer = raw_input("Your answer: ")
    if answer == "pig":
        print "You got it!"
    else:
        print "Nope! Game over."  

print "Thanks for playing! Hope to see you again soon!"