import re

print("CMS Signup")
print("-"*40)
ltCheck = []


def validateInput():
    name = input("Enter your name : ")
    ltCheck.append(re.search('^[A-za-z]', name))
    # print(m)
    # print(m.group(0))

    # # digits
    phoneNum = input("Enter your phone number : ")
    ltCheck.append(re.search('(\d{10})', phoneNum))

    # email
    email = input("Enter your email : ")
    pattern = r"^[a-z]+[-_$.a-z]*@[a-z]*\.[a-z]+$"
    ltCheck.append(re.search(pattern, email))

    # date
    date = input("Enter DOB in dd/mm/yy : ")
    ltCheck.append(re.search(r'(\d+/\d+/\d+)', date))


validateInput()
print(ltCheck)
if None in ltCheck:
    print("SignUp Failed")
else:
    for i in ltCheck:
        print(i.group(0))
