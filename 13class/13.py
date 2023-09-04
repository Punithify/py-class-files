# excextion handling
# print(10 * (1/0))
import os
try:
    # x = int(input("Please enter a number: "))
    1/0
except ZeroDivisionError as err:
    print("Oops! That was no valid number.  Try again...", err)


print("continue exceution")

# os error
try:
    print("try")
    f = open("file.txt")
    print("-"*40)
    s = f.readline()
    i = int(s)
    print(i)
except FileNotFoundError as e:
    print(f"FileNotFoundError successfully handled\n"
          f"{e}")
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")

# index out of bound
