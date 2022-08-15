#Set is a collection which is unordered and unindexed. No duplicate members.


thisset = {"apple", "banana", "cherry"}
print(thisset)



thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)



thisset = {"apple", "banana", "cherry"}

print(len(thisset))



thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)



thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)



thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists




set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)



set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)




######frozenset####

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)


mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
x[1] = "strawberry"
print(x)



Student = {"name": "Ankit", "age": 21, "sex": "Male",  
           "college": "MNNIT Allahabad", "address": "Allahabad"} 
  
# making keys of dictionary as frozenset 
key = frozenset(Student) 
  
# printing keys details 
print('The frozen set is:', key)
