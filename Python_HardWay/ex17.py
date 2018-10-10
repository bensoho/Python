#ex17.py
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" %(from_file,to_file))

# we could do these two on one line too, how?
inputed= open(from_file)
indata = inputed.read()
print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

output = open(to_file,'w')
output.write(indata)
output.write("test data has wrote in.\n")
print("Alright, all done.")
output.close()
inputed.close()