# dictionary

# dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.


tele = {"hello": 78999, "ram": 8900}
# print(tele["jack"])
print(list(tele))
# print(tele[("hello", "world")])
# print(tele[["m", "n"]]) list cannot be used as keys
print("-" * 40)

print(tele.get('ram'))
print(tele.keys())
print(tele.values())
print(id(tele.update({"ram": 9990})))
print(id(tele.update({"update-item": "update-item"})))
print(tele.pop("ram"))
print(tele)
tele["new"] = "new-item"
del tele["update-item"]


print("-" * 40)

# print("-", 30)
print(tele.items())
for x in tele.items():
    print(x)


# creating dictionary using dict keyword
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# print(tele)

print("-"*40)


def dictDisplay(**d):
    print(d)


dictDisplay(new=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
