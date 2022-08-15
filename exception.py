"""
try:
	You do your operations here
	......................

except ExceptionI:
	If there is ExceptionI, then execute this block.
except ExceptionII:
	If there is ExceptionII, then execute this block.
	......................
else:
	If there is no exception then execute this block.

"""



try:
  print(x)
except:
  print("An exception occurred")


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")




try:
	fh = open("testfile", "r")
	fh.write("This is my test file for exception handling!!")
except IOError:
	print ("Error: can\'t find file or read data")
else:
	print ("Written content in the file successfully")




try:
	fh = open("testfile", "w")
	fh.write("This is my test file for exception handling!!")
except IOError:
	print ("Error: can\'t find file or read data") 
else:
	print ("Written content in the file successfully")
fh.close()




try:
	fh = open("testfile", "w")
	fh.write("This is my test file for exception handling!!")
finally:
	print ("Error: can\'t find file or read data")
fh.close()





x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")



x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")




def functionName( level ):
	if level <1:
	  raise Exception(level)
	  # The code below to this would not be executed
	  # if we raise the exception
	return level
try:
	l=functionName(-10)
	print ("level=",l)
except Exception as e:
	print ("error in level argument",e.args[0])

