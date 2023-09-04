dictNew=dict(interface=["ethernet-1","ethernet-2"], IP=["1.1.1.1","2.2.2.2"], status=["up","down"])

print(dictNew)
# user=input("enter a interface")

# for i in dictNew:
#     print(list(dictNew[i]))

print([dictNew])

for i in dictNew:
    print(i)