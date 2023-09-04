# functions
# 1. it is declared with the keyword "def"

def doSomething(a, b=0):
    return a+b


def doSomethingElse(a=4, b=2):
    return a-b


print(doSomething(2)+doSomethingElse())

# positional Parameters


# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action)
#     print("if you put", voltage)
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")


# parrot(1000)
# parrot(voltage=1000000, action='VOOOOOM')
# parrot(action='VOOOOOM', voltage=1000000)
# parrot('a million', 'bereft of life', 'jump')
# parrot('a thousand', state='pushing up the daisies')


def imageUpload(*file):
    print("imageUpload", file)


imageUpload(["img", "resolution"], (1, 2, 34))

# **name
# accept any number of arguments


def cheeseShop(*images, **menu):
    # print(images)
    # print(menu)
    for t in images:
        print(t)
    print("-" * 40)
    for i in menu:
        print("menu-item", menu[i])


cheeseShop([121212121212, 222, "hello"], (1, 2, 3), shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def imageUpload(*file):
    print(file)


# imageUpload(["img", "resolution"], (1, 2, 34))
