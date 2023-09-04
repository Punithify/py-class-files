
import string
from operator import itemgetter
# domianDesc = "A Content Management System CMS is a powerful software application designed to simplify the creation, management, and publication of digital content on websites. It provides users, whether they are individuals or organizations, with a user-friendly interface to effortlessly handle various aspects of content, such as writing, editing, organizing, and scheduling. CMS platforms enable multiple users to collaborate seamlessly, facilitating efficient workflows for content creation and approval processes. With its diverse array of tools and templates."

# print("Number of occurence of the word 'CMS' : ", domianDesc.count("CMS"))

# countChar = 0
# for i in domianDesc:
#     if (i == ',' or i == ' ' or i == '.'):
#         pass
#     else:
#         countChar += 1

# print("Number of characters in the above description is : ", countChar)

# print("Number of words in the above description is : ",
#       len(domianDesc.split(' ')))  # number of words
# print("Number of lines in the above description is : ",
#       len(domianDesc.split('.')))  # number of sentences


# b

# domainName = "content management system"
# n = int(input("Enter the add number"))
# indexList = []
# domainName.split(' ')
# for i in domainName:
#     if (string.ascii_lowercase.find(i) >= (26-n)):
#         i = 'a'
#     indexList.append(string.ascii_lowercase[(
#         string.ascii_lowercase.find(i))+n])
# print("Encrypt Method:value of n = ", n)
# print("Encrypted string is : ", "".join(indexList))


# 2.

# def pay(hourlyWage, WorkHour):
#     if WorkHour > 40:
#         return (hourlyWage*1.5)*WorkHour
#     return hourlyWage*WorkHour


# hourlyWage, workHour = [float(s) for s in
#                         input("enter hourly wage and work hour of the employee ").split(' ')]
# print("employee's pay : ", pay(hourlyWage, workHour))


# 3.
houseList = [('main st.', 4, 4000), ('elm st.',
                                     1, 1200), ('pine st.', 2, 1600)]
streetName = []
numVal = []
rentList = []
for i in houseList:
    streetName.append(i[0])
    numVal.append(i[1])
    rentList.append(i[2])
print("alphabetical order of string value(Street Name) : ", sorted(streetName))
print("descending order by first numeric value : ", sorted(numVal))
print("descending order by second numeric value (Rent) :",
      sorted(rentList, reverse=True))

# using itemgetter

print("alphabetical order of string value(Street Name) : ",
      sorted(houseList, key=itemgetter(0)))
print("Acending order by first numeric value : ",
      sorted(houseList, key=itemgetter(1)))
print("descending order by second numeric value (Rent) :",
      sorted(houseList, key=itemgetter(2), reverse=True))
