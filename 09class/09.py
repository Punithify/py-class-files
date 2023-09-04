# oops concepts


class SampleClass:
    stat = "A simple class"

    def fun():
        return "hello"

    def __init__(self, name):
        self.name = name
        self.stat = name
        # self.sample_dict = dict(1:name)
        print(self)


x = SampleClass("someName")
y = SampleClass("otherName")
print(x.stat)
# print(x.fun())
print(x.name)


# inheritance

class Account:
    def f1():
        print("from parent class")


class AccountSub(Account):
    def f2():
        print("from child class")


obj = AccountSub
obj.f1()
