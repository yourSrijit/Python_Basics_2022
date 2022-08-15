#---if
a = 33
b = 200

if b > a:
  print("b is greater than a")

#---shorthand If
a = 200
b = 33
if a > b: print("a is greater than b")


#---if-else
a = 33
b = 33
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")


#---shorthand if-else
a = 2
b = 330
print("A") if a > b else print("B")


#---if-else-elseif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#--Ternary Operators

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#--Nested If

num=int(input("enter number"))
if num%2==0:
	if num%3==0:
		print ("Divisible by 3 and 2")
	else:
		print ("divisible by 2 not divisible by 3")
else:
	if num%3==0:
		print ("divisible by 3 not divisible by 2")
	else:
		print ("not Divisible by 2 not divisible by 3")


#----maximum between 3 number

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b:
  if a>c:
    print(a,' is maximum')
  else:
     print(c,' is maximum')
else:
  if b>c:
    print(b,' is maximum')
  else:
     print(c,' is maximum')







#---pass
#having an empty if statement like this, would raise an error without the pass statement
a = 33
b = 200

if b > a:
  pass



#----switchcase

def switch(i):
        return{
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }.get(i,"Invalid day of week")
	
	 
day=switch(5)
print(day)

def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)

print(f('a'))



def zero():
        return 'zero'
def one():
        return 'one'
def indirect(i):
        switcher={
                0:zero,
                1:one,
                }
        func=switcher.get(i,'Invalid')
        return func()

print(indirect(1))



def add():
        x=2+3
        return x
def mul():
       x=2*3
       return x

def indirect(i):
        switcher={
                0:add,
                1:mul,
                }
        func=switcher.get(i,lambda:'Invalid')
        return func()

n=int(input('enter :'))
print(indirect(n))










