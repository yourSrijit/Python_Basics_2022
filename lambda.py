#Lambda forms can take any number of arguments but return just one value in the 
form of an expression. They cannot contain commands or multiple expressions.

#An anonymous function cannot be a direct call to print because lambda requires an 
expression.

#Lambda functions have their own local namespace and cannot access variables 
other than those in their parameter list and those in the global namespace.

#Although it appears that lambdas are a one-line version of a function, they are not 
equivalent to inline statements in C or C++, whose purpose is to stack allocation
by passing function, during invocation for performance reasons.



x = lambda a: a + 10
print(x(5))


x = lambda a, b: a * b
print(x(5, 6))



x = lambda a, b, c: a + b + c
print(x(5, 6, 2))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))