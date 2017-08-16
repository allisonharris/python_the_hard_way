# this lets us use argv
from sys import argv

# this tells us what we must type into the command line
script, input_file = argv

# this defines print_all as reading the file from the beginning, takes an argument of f
def print_all(f):
	# print the contents of the file
	print f.read()

# this defines rewind as moving to the start of the file, takes an argument of f
def rewind(f):
	# seek(0) moves the file to the first byte in the file
	f.seek(0)

#this defines print_a_line function which needs 2 arguments
def print_a_line(line_count, f):
	# print line_count, then print a line from file f
	print line_count, f.readline()

# sets the current_file to the input_file
current_file = open(input_file)

# print message with line break
print "First let's print the whole file:\n"

# print all contents of current_file
print_all(current_file)

# print message
print "Now let's rewind, kind of like a tape."

# go back to the first byte of the current_file
rewind(current_file)

# print message
print "Let's print three lines:"

# set current_line to 1
current_line = 1
# print '1' followed by print first line of current_file 
print_a_line(current_line, current_file)

# set current_line to itself plus 1
current_line += current_line 
# print '2' followed by second line of current_file
print_a_line(current_line, current_file)

# set current_line to itself plus 1
current_line += current_line 
# print a '3' followed by the third line of current_file
print_a_line(current_line, current_file)