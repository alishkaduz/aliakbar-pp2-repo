from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map(): square each number
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter(): keep even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# reduce(): sum of all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)









names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

# enumerate()
for index, name in enumerate(names):
    print(index, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)






value = "123"

# Type checking
print(isinstance(value, str))

# Type conversion
num = int(value)
print(num, type(num))

float_num = float(num)
print(float_num, type(float_num))