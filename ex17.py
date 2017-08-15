from sys import argv
from os.path import exists
open(raw_input("To file? "), 'w').write(open(raw_input("From file? ")).read())

# the following code was the original code from the exercise
# I was able to condense the code into three lines as seen above


#script, from_file, to_file, = argv

#print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#print "Alright, all done."

#out_file.close()
#in_file.close()