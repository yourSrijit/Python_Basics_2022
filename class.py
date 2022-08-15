class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)




class MyClass:
  x = 5
  def display(self):
    print(self.x)

p1 = MyClass()
p2 = MyClass()

p1.x=10
p1.display()
p2.display()


#public access specifier
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age



p1 = Person("John", 36)
print(p1.name)
print(p1.age)




#protected access specifier

class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age



p1 = Person("John", 36)
print(p1.name)
print(p1.age)





#private access specifier
class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  def display(self):
    print(self.__name,self.__age)



p1 = Person("John", 36)
print(p1.name) #error
print(p1.age)	#error
display()







p1.age = 40
print(p1.age)

del p1
print(p1)




class Point:
	def __init( self, x=0, y=0):
	self.x = x
	self.y = y
	def __del__(self):
		class_name = self.__class__.__name__
		print (class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3))# prints the ids of the obejcts
del pt1
del pt2
del pt3
When the above code is executed, it pro






class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()




class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()







#like static
class Employee:
	empCount = 0
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	def displayCount(self):
		print ("Total Employee %d" % Employee.empCount)
	def displayEmployee(self):
		print ("Name : ", self.name, ", Salary: ", self.salary)


#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)