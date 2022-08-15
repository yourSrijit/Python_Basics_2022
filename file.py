


fo = open("foo.txt", "w")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()


fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close()	# Close opend file



fo = open("foo.txt", "r")
str = fo.read(10)
print ("Read String is : ", str)
# Close opened file
fo.close()



fo = open("foo.txt", "r")
str = fo.read(10)
print ("Read String is : ", str)

position = fo.tell()		# Check current position
print ("Current file position : ", position)

position = fo.seek(0, 0)	# Reposition pointer at the beginning once again
str = fo.read(10)
print ("Again read String is : ", str)

fo.close()		# Close opened file




import os
# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )
# Delete file test2.txt
os.remove("text1.txt")




#-----Assuming that 'foo.txt' contains following lines
C++
Java
Python
Perl
PHP


fo = open("foo.txt", "r")
print ("Name of the file: ", fo.name)
for index in range(5):
line = next(fo)
print ("Line No %d - %s" % (index, line))
# Close opened file
fo.close()






#-----Assuming that 'foo.txt' file contains the following text:
This is 1st line
This is 2nd line
This is 3rd line
This is 4th line
This is 5th line

fo = open("foo.txt", "r")
print ("Name of the file: ", fo.name)
line = fo.read(10)
print ("Read String is : ", line)
# Close opened file
fo.close()

fo = open("foo.txt", "r")
print ("Name of the file: ", fo.name)
line = fo.readline()
print ("Read String is : ", line)
fo.close()


fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)
line = fo.readline()
print ("Read Line: %s" % (line))
line = fo.readline(16)
print ("Read Line: %s" % (line))
# Close opened file
fo.close()





"""seek(offset[, whence])


offset- This is the position of the read/write pointer within the file.

whence- This is optional and defaults to 0 which means absolute file positioning, 
other values are 1 which means seek relative to the current position and 2 means 
seek relative to the file's end.

"""

#-----Assuming that 'foo.txt' file contains the following text:


This is 1st line
This is 2nd line
This is 3rd line
This is 4th line
This is 5th line



fo = open("abc.txt", "r+")
print ("Name of the file: ", fo.name)
str = "This is 6th line"
# Write a line at the end of the file.
fo.seek(0, 2)
line = fo.write( str )
# Now read complete file from beginning.
fo.seek(0,0)
for index in range(6):
line = next(fo)
print ("Line No %d - %s" % (index, line))
# Close opened file
fo.close()



