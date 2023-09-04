import re
# ?
# res = re.search('colou?r', 'colour are great')
# print(res.group(0))


res = re.search('[0-1]', "1 is a great number")
res = re.search('\d', "1 is a great number")

print(res.group(0))
