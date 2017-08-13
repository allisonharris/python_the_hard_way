# import the argument variable module
from sys import argv

# to run the program, need to enter the script name and filename
script, filename = argv

# txt will open up the contents of the filename
txt = open(filename)

# print message of the contents of file
print "Here's your file %r:" % filename
# print out the contents of the file
print txt.read()
txt.close()

# prompt user to input the filename again and print it with a '> ' before the filename
print "Type the filename again:"
file_again = raw_input("> ")
# open the file that the user input
txt_again = open(file_again)

# print out the contents of the file
print txt_again.read()
txt.close()