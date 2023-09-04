# sets

operations = {"add", "sub", "div"}


items = {x for x in operations}
print(items)

for x in operations:
    print(x)

operations.add("new-item")
operations.add("new-item1")

print(operations)
print("-"*40)

operations.update({"check": "new", 1: "hello"})
print(operations)
print("-"*40)
print(operations)
# operations.remove("sub")
operations.discard("add1")
# operations.pop()
print(operations)
print(all(operations))  # checks the set is empty
print(any(operations))  # checks if there is any element

# frozen set
print("-"*40)

fset = frozenset(operations)  # immutable set
print(id(fset))
