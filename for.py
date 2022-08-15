for x in range(6):
  print(x) 


for x in range(2, 6):
  print(x) 


for x in range(2, 30, 3):
  print(x) 


for x in "banana":
  print(x) 


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 



#---break

for letter in 'Python': 
	if letter == 'h':
		break
	print ('Current Letter :', letter)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

#---contine

for letter in 'Python': 
	if letter == 'h':
		continue
	print ('Current Letter :', letter)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 



#---else_with_for

for x in range(6):
  print(x)
else:
  print("Finally finished!")


numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
	if num%2==0:
		print ('the list contains an even number')
		break
else:
	print ('the list doesnot contain even number')


#-----nested for

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

#----pass statement
# having an empty for loop like this, would raise an error without the pass statement

for x in [0, 1, 2]:
  pass
print('hello')


for letter in 'Python':
	if letter == 'h':
		pass
		print ('This is pass block')
	print ('Current Letter :', letter)
print ("Good bye!")
