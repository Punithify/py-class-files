import random
# import math
# import cmath
names = ["bob", "rob", "job"]
print("bob" in names)


# random


# Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
print(random.uniform(10, 20))

# precedence opertor


print(1+3*2-5+4)

print(1+3*(2-5+4))
print(5**2**2*3+1)
print(5**(2**2))
print(1+3/5)


# B
# print(math.pow(10, 5))
# print(math.sqrt(10))
# # x2-7x+10=0
# a = int(input("enter values of a"))
# b = int(input("enter values of b"))
# c = int(input("enter values of c"))

# discrement = b**2-4*a*c
# posSol = str((-b+cmath.sqrt(discrement))/(2*a))
# negSol=str((-b-cmath.sqrt(discrement))/(2*a))
# print(posSol,negSol)


# f to c

# temp = float(input("Enter temperature in Fahrenheit: "))
# celsius = (temp - 32) * 5/9
# print(celsius)

# print(1.0/7)


# strings
# name = "bob"
# print(name[-2:1``])

# find a number game

# number = int(input("enter a number"))
# genNum = random.randint(0, 5)

# while (genNum):
#     number = int(input("enter a number"))
#     print(genNum)
#     if number == genNum:
#         print("Winner")
#         exit()
#     elif number > genNum:
#         print("Entered num is greater than rand num")
#     elif number < genNum:
#         print("entered num is less than rand num")

# John deposited an initial sum of Rs.3000 in his account. After 3 years,
# the balance reaches Rs.3335.8 due to composite interest. What is the
# interest rate per annual?

# print()


# check if a year is a leap yesr

def leapYear(year):
    if (year % 400 == 0 or year % 100 != 0 and year % 4 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


leapYear(2000)
