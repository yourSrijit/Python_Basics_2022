class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()




#private-protected-public access specifier

class Super: 
      
     # public data member 
     var1 = None
  
     # protected data member 
     _var2 = None
       
     # private data member 
     __var3 = None
      
     # constructor 
     def __init__(self, var1, var2, var3):   
          self.var1 = var1 
          self._var2 = var2 
          self.__var3 = var3 
      
    # public member function    
     def displayPublicMembers(self): 
   
          # accessing public data members 
          print("Public Data Member: ", self.var1) 
         
     # protected member function    
     def _displayProtectedMembers(self): 
   
          # accessing protected data members 
          print("Protected Data Member: ", self._var2) 
       
     # private member function    
     def __displayPrivateMembers(self): 
   
          # accessing private data members 
          print("Private Data Member: ", self.__var3) 
  
     # public member function 
     def accessPrivateMembers(self):      
            
          # accessing private memeber function 
          self.__displayPrivateMembers() 
   
# derived class 
class Sub(Super): 
   
      # constructor  
       def __init__(self, var1, var2, var3):  
                Super.__init__(self, var1, var2, var3) 
            
      # public member function  
       def accessProtectedMemebers(self): 
                  
                # accessing protected member functions of super class  
                self._displayProtectedMembers() 
   
# creating objects of the derived class      
obj = Sub("Geeks", 4, "Geeks !")  
  
# calling public member functions of the class 
obj.displayPublicMembers() 
obj.accessProtectedMemebers() 
obj.accessPrivateMembers()  
  
# Object can access protected member 
print("Object is accessing protected member:", obj._var2) 
  
# object can not access private member, so it will generate Attribute error 
#print(obj.__var3) 




#---constructuctor overide
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()



#-----method overide
class Parent: 			# define parent class
	def myMethod(self):
		print ('Calling parent method')
class Child(Parent):		 # define child class
	def myMethod(self):
		print ('Calling child method')
c = Child() 			# instance of child
c.myMethod() 			# child calls overridden method




#---overload operator
class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __str__(self):
		return 'Vector (%d, %d)' % (self.a, self.b)
	def __add__(self,other):
		return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)


#supper keyword

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()



"""
class A: # define your class A
.....
class B: # define your calss B
.....
class C(A, B): # subclass of A and B
.....
"""



class firstname:
  def __init__(self, fname):
    self.firstname = fname
  def printname1(self):
    print(self.firstname, end="")
    
class lastname:
  def __init__(self,lname):
      self.lastname = lname
  def printname2(self):
    print(" "+self.lastname)

class Student(firstname,lastname):
   def __init__(self, fname,lname):
       firstname.__init__(self, fname)
       lastname.__init__(self, lname)

x = Student("Mike", "Olsen")
x.printname1()
x.printname2()


"""
class A: # define your class A
.....
class B(A): # define your calss B
.....
class C(B): # subclass of A and B
.....


class firstname:
  def __init__(self, fname):
    self.firstname = fname
  def printname1(self):
    print(self.firstname, end="")
    
class lastname(firstname):
  def __init__(self,fname,lname):
       super().__init__(fname)
       self.lastname = lname
  def printname2(self):
    print(" "+self.lastname)

class Student(lastname):
   def __init__(self, fname,lname):
       super().__init__(fname,lname)
      

x = Student("Mike", "Olsen")
x.printname1()
x.printname2()





