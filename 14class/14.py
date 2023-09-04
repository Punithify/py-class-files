# a stockbroker recieves from his client instructions to buy and sell shares understands the instructions and competes the trading but finds it display amount of spent on buying and the total amount received by selling as a tuple.So you help broker by printing it as a string.Consider the explanation and following test case:
# Input is a tuple that contains tuple as elements
# Each element in the tuple will have Company initials ,quamtity,price,and status where stis arts buy(b) or sell(s)
# if the input is (("ABC",300,453.0,"b").("XYZ",120,298.5,"s").("ASD"29,45.5,"s").("QWE",160,23.7,"b"))
# output will be
# {"buy's:139692,'sell':37139.5,'buysqty':460,'sellqty:149}
#        if the input is empty tuple print"buys:0 sell:0"
#        If the input is not as per the format required for example
#        {SDF,200,4.5,"I"}print "invalid input


stockBroker = (("ABC", 300, 453.0, "b"), ("XYZ", 120, 298.5,
                                          "s"), ("ASD", 29, 45.5, "s"), ("QWE", 160, 23.7, "b"))

print(stockBroker)
for i in stockBroker:
    print(i)
    for e in [i]:
        print(dict([("buys", e[1]*e[2]), ("sell", ""),
              ("buysqty", ""), ("sellqty", "")]))
        # print(dict([("buys", )]))
