#Syntax: lambda arguments : expression
x = lambda a : a + 10
print(x(5)) 

#Lambda functions can take any number of arguments:
x = lambda a, b : a * b
print(x(5, 6)) 

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11)) 


#The filter() function creates a list of items for which a function returns True:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


#The sorted() function can use a lambda as a key for custom sorting:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)