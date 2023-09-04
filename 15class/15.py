# regular expression

import re

# Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object
sample = "the dog is singing"
res = re.match("the", sample)
print(res.group(0))


# If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object

m = re.search('def', 'abcdef')
# print(m)
print(m.group(0))


# The string is scanned left-to-right, and matches are returned in the order found

print(re.findall('[z]', "zoo is near the palace zoo"))


print(re.sub('a', 'b', "Hey i Am  and a")
      )

# forming a search pattern

# res = re.search("\$", "$ A food is a 5 ")
# if the string as the given pattern, returns the re expression
res = re.search("^food", "food is a 5 ")

print(res.group(0))

print(re.search("hello{1}", "hello from python class").group(0))
