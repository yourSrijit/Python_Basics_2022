def push(top,max):                                                               
    if((top==(max-1))):
        print('stack is full')
    else:
        top=top+1
        x=int(input("enter the  data :"))
        stack.insert(top,x)
    return(top)
    
    
def pop(top):
    if(top==-1):
        print('stack is empty')
    else:
        x=stack.pop(top)
        print('deleted data is :',x)
        top=top-1
    return top

def display(top):
    if((top==-1)):
        print('stack is empty')
    else:
        print('stack elements are :')
        for i in reversed(range(len(stack))):
            print(stack[i])

stack=[]
top=-1
max=int(input("enter the  maxsize :"))
while(1):
    print('1.push\n2.pop\n3.display\n4.exit\n')
    i=int(input("enter your choice :"))
    if(i==1):
        top=push(top,max)
    elif (i==2):
        top=pop(top)
    elif (i==3):
        display(top)
    elif (i==4):
        break
    else:
        print("wrong choice")
