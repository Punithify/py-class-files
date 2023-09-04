# Create a list ,get value n from the user,check value n present in th table
# if it is present generate table for n,if n is not in list consider n as a index postion


randList=[1,2,3,5]
n=7
# print(randList.index(n)>=len(randList))

for n in randList:
    # if(n in randList):
    #     for i in range(1,11):
    #         print(n*i)
    # else:
    for n in range(len(randList)):
        print(randList.index(n))