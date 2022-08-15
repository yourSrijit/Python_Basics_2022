var1 = 'Hello World!'
var2 = "Python Programming"
print(var1)
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#--update string
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')


#--------function

a = "Hello, World!"
print(len(a))


#--palindrome programe-----
n=input("enter the string")
j=len(n)-1
i=0
while i<=j:
    if(n[i]!=n[j]):
        break
    i+=1
    j-=1
if i>j:
    print("palindrome")
else:
    print("not palindrome")




a = " Hello, World! "
print(a.strip())


a = "Hello, World!"
print(a.lower())

a = "Hello, World!"s
print(a.upper())


a = "Hello, World!"
print(a.replace("H", "J"))


a = "Hello, World!"
b = a.split(",")
print(b)


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) 


txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 



a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity=20
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 


txt = "We are the so-called \"Vikings\" from the north."
print(txt) 


txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)


txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)



txt = "banana"
x = txt.center(20)
print(x)



txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)




txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)




txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)





txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)

txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)




txt = "Company12"

x = txt.isalnum()

print(x)

txt = "Company 12"

x = txt.isalnum()

print(x)




txt = "CompanyX"

x = txt.isalpha()

print(x)]


txt = "50800"

x = txt.isdigit()

print(x)


txt = "hello world!"

x = txt.islower()

print(x)


txt = "565543"

x = txt.isnumeric()

print(x)



txt = "   "

x = txt.isspace()

print(x)



txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)



txt = "THIS IS NOW!"

x = txt.isupper()

print(x)



myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)



txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)




txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)


txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

txt = "Hello, welcome to my world."

x = txt.rindex("e", 5, 10)

print(x)


txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)


txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)



txt = "Welcome to my world"

x = txt.title()

print(x)


str = "this2016"
print (str.isdecimal())
str = "23443434"
print (str.isdecimal())




