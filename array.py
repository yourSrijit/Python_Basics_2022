array = [1,2,3,4,5]
print(array)


cars = ["Ford", "Volvo", "BMW"]
print(cars)

x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars)

x = len(cars)
print(x)


fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)




fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)




cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)



cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)

cars.pop(1)

print(cars)


cars = []

cars.append("Honda")
cars.append("BMW")
cars.append("AUDI")

print(cars)




cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)




fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)






cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)


cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)





fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)



fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)




fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)




fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)


fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

print(fruits)


#---linear search
n=int(input('enter'))
print('enter the data')
a=[]
for i in range(n):
   a.append(int(input('enter')))
key=int(input('enterh key'))
for i in range(n):
  if a[i]==key:
    f=1
    break
if f==1:
 print('value found at ',i,'position')
else:
 print('value not found')






R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
matrix = [] 
print("Enter the entries rowwise:") 
  # For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries
     print('enter the data for row',i,' col',j,' :',end = '')
     X=int(input())
     a.append(X) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 


"""
#---display in another way
for i in matrix:
    print(i)
"""





