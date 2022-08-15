#---while

count = 0
while (count < 9):
	print ('The count is:', count)
	count = count + 1
print ("Good bye!")


#---break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print ("Good bye!")


#---continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#---else_with_while

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print(i," is no longer less than 6")


#----infiniteloop
var = 1
while var == 1 : 		
	num = int(input("Enter a number :"))
	print ("You entered: ", num)
print ("Good bye!")