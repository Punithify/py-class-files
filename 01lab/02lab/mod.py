padList=['10000000','01000000','001000000',"00010000","00001000"]

binList=[]
def encodeQR(productName):
    for i in productName:
        binList.append(bin(ord(i))[2:])
    for i in range(len(binList)):
        binList[i]=binList[i]+padList[i]

    return binList