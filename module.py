
#----mymodule.py
def greeting(name):
  print("Hello, " + name)


import mymodule

mymodule.greeting("Jonathan")



#----mymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


import mymodule

a = mymodule.person1["age"]
print(a)

#---rename
import mymodule as mx

a = mx.person1["age"]
print(a)



#----mymodule.py
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from mymodule import person1
print (person1["age"])

print(greeting("ajay")) #error

