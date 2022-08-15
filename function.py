def sum(a,b):
    z=a+b
    return(z)


   
def mul(a,b):
    z=a*b
    return(z)
   
a=int(input('enter a :'))
b=int(input('enter b :'))
c=sum(a,b)
print('sum is : ',c)
m=mul(a,b)
print('mul is : ',m)





def main():
    print("hello world!")

if __name__ == "__main__":
    main()

print("Guru99")





def my_function():
  print("Hello from a function")

my_function()




def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")




def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")




def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)






def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))





def myfunction():
  pass
myfunction():




def changeme( mylist ):
	print ("Values inside the function before change: ", mylist)
	mylist[2]=50
	print ("Values inside the function after change: ", mylist)
	return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)





def changeme( mylist ):
	mylist = [1,2,3,4] # This would assi new reference in mylist
	print ("Values inside the function: ", mylist)
	return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)





def printme( str ):

	print (str)
	return

printme( str = "My string")



def printinfo( name, age ):

	print ("Name: ", name)
	print ("Age ", age)
	return

printinfo( age=50, name="miki" )




#---global_local
total = 0 # This is global variable.

def sum( arg1, arg2 ):

	total = arg1 + arg2; # Here total is local variable.
	print ("Inside the function local total : ", total)
	return total

sum( 10, 20 )
print ("Outside the function global total : ", total )




#----recursion
def factorial(n):
  if n==1:
    return 1
  else:
    f=n*factorial(n-1)
  return (f)

print(factorial(5))