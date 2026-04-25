#In Python, a function is defined using the def keyword, followed by a function name and parentheses:
def my_function():
  print("Hello from a function") 

# To call a function, write its name followed by parentheses:
my_function()


#Valid function names:
# calculate_sum()
# _private_function()
# myFunction2()



#The following example has a function with one argument (fname). When the function is called, 
# we pass along a first name, which is used inside the function to print the full name: 
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.

#You can send arguments with the key = value syntax.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy") 