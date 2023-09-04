# inheritence
# tyoes of inheritence
# 1. single inheritence
# 2. mutiple inheritence- more than one parent class
# 3. multilevel inheritence
# 4. heirachical inheritence
# 5. hybrid inheritence


from abc import ABC, abstractmethod


class Media:
    def __init__(self, fileExt):
        self.fileExt = fileExt
        # self.fileSize = fileSize
        print(fileExt)
        print("construter invoked")

    def displayMedia(self):
        print(self.fileExt)
        print(self.fileSize)


class Provider(Media):

    def __init__(self, fileExt):
        super().__init__(fileExt)

    # def display(self, pos):
    #     super(Provider, self).__init__(pos)
        # Media.__init__(self, pos, pos1)


# media = Media()
# media.displayMedia()
# provd = Provider(".png")
# provd.display()

print("-"*40)
# multiple inheritence

# class A:
#     def fun(self):
#         print("from class A")


# class B:
#     def fun1(self):
#         print("From class B")


# class C(A, B):
#     def fun2(self):
#         print("from class C")


# cobj = C()
# cobj.fun()

# print("-"*40)


# class A:
#     def fun(self):
#         print("from class A")


# class B(A):
#     def fun1(self):
#         print("From class B")


# class C(B):
#     def fun2(self):
#         print("from class C")


# obj = C()
# obj.fun1()

# obj = B()
# obj.fun()


# hybrid inheritence
print("-"*40)


class A:
    def fun(self):
        print("from class A")


class B(A):
    def fun1(self):
        print("from class B")


class C:
    def fun2(self):
        print("from class C")


class D(B, C):
    def fun3(self):
        print("from class D")


dobj = D()
dobj.fun()
dobj.fun1()

print("-"*40)
# abstract class


# class MyABC(ABC):
#     pass
# class Foo:
#     def fun(self):
#         print("from added")


class MyAbtractClass(ABC):
    @abstractmethod
    def fun(self):
        pass


class MyImplemntation(MyAbtractClass):
    def fun(self):
        print("MY implementation")


imp = MyImplemntation()
imp.fun()
