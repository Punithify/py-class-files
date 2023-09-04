from datetime import datetime,date
import re
allowed_characters = set("0123456789/")
def validateDateFormat(year,month,day):
    try:
        print("Entered Date is :" ,date(year,month,day))
        today = datetime.today()
        print("Given date is Vaild Format")
        return "Your Age is : ",today.year - year 
         
    except ValueError:
        print(" pls enter date in the format dd/mm/yy")

values=[i for i in input("Enter day, month, year in dd/mm/yyyy format : ")]
formatList=[]
for i in values:
    if i not in allowed_characters:
        print("Pls enter the name in dd/mm/yyyy format")
    if(re.search("^[a-zA-Z ]*$",i)):
        raise Exception('user exception', 'Bye ! Hope to see u again')
values="".join(values).split('/')
for i in values:
    formatList.append(int(i))
# print(formatList)

print(validateDateFormat(formatList[2],formatList[1],formatList[0]))
