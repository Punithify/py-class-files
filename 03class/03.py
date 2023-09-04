# sequeces in python
# list,tuple and range

# 1. tuples

# A tuple consists of a number of values separated by commas,


t = (12345, 'hello!', True, "bob")
print(type(t))


# Tuples are immutable:
# t[0] = "bob"  # error

print(t[-1])
print(t[3:4])
print(t[-2:-1])
print(t[-5:])  # full tuple
print(t[-5:-1])

# but they can contain mutable objects:

t_obj = ([1, 2, 3], [3, 2, 1])

print(t_obj)

# create three tuples based on ur domain


# 2. conversion
names = ["dheera", "ee", "sultana"]
names1 = ["ram", "sham"]
nums = (1, 2, 3)
print(list(t_obj))
print(id(t_obj))
# print(id(names))
# print(id(names1))
print


# 3. range

# The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops

print(list(range(1, 11)))  # excludes the second value

print(list(range(0, 30, 5)))
# first arg-start
# second arg-stop
# thrid arg-step

tr = range(0, 20, 2)
print(tr)


# 4.list

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))  # number of occurence of apple
fruits.append("winner")
# print(fruits.copy())
names = ["bob", "rob", "job"]
fruits.extend(names)  # appends two list
fruits.pop()  # pops out the last element of the list
fruits.remove('orange')  # removes a element based on the value
del fruits[2]
print(fruits)

squares = []

for x in range(10):
    squares.append(x**2)

print(squares)

a = ("dheera", "ee")
b = [1, 23, 3]
c = b.extend(a)
print(c)  # error-only list type can be passed
