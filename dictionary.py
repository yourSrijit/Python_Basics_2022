#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

thisdict["year"] = 2018

print(thisdict)

dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" % dict.keys())


dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print ("Values : ", list(dict.values()))


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


print(len(thisdict))

for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)


thisdict.pop("model")
print(thisdict)



x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)



del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)



mydict = thisdict.copy()
print(mydict)


mydict = dict(thisdict)
print(mydict)


dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print ("updated dict : ", dict)



#neste Dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)




child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)






roll name marks
1    ajay  48
2     bijay 98








