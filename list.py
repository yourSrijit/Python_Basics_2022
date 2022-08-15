#List is a collection which is ordered and changeable. Allows duplicate members.

thislist = [1,2,3,4,5,6,7]
print(thislist)


list2=list(range(5)) #creates list of numbers between 0-4
print(list2)



thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
print(thislist[-1])
thislist[1] = "blackcurrant"   
print(thislist)


thislist = list(("apple", "banana", "cherry")) #list constructor
print(thislist)


list2=list(range(5)) #creates list of numbers between 0-4
print(list2)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4]
print(thislist[2:])
print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print(len(thislist))

thislist.append("orange")
print(thislist)

thislist.insert(1, "mango")
print(thislist)

thislist.remove("banana")
print(thislist)

thislist.pop()
print(thislist)


del thislist[0]
print(thislist)

del thislist
print(thislist)


fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)



thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)



fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)


cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

cars.sort(reverse=True)

print(cars)



list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))

print ("Max value element : ", min(list1))
print ("Max value element : ", min(list2))



aTuple = (123, 'C++', 'Java', 'Python')
list1 = list(aTuple)
print ("List elements : ", list1)
str="Hello World"
list2=list(str)
print ("List elements : ", list2)





