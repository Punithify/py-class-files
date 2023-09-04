# mutable and immutable

# lambda
# lambda [parameters]: expression
# def multiply(x, y):  x*y

# sum=lambda x,y=0: print(x+y)


# print(multiply(1, 2))
# sum(1)


# def find(x, y, z=0, w=0): print(x+2*x+3*z+4*w)


# find(1, 2)
# f(1,2,3)

# write a function using lamdha calculate the x3+y2+5,assign x and y with default args


# def cal(x=3, y=2): return x**3+y**2+5


# print(cal())

# List Comprehensions
# List comprehensions provide a concise way to create lists.

squares = []
for x in range(1, 6):
    squares.append(x**2)

print(squares)
newList = [i for i in squares]
print(newList)
freshfruit = ['banana', 'loganberry', 'passion fruit']
print([x for x in freshfruit if x in 'banana'])
# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(1, 10)])

print("-"*40)
