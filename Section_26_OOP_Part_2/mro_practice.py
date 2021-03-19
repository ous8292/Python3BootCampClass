class A:
    def do_something(self):
        print("Method Defined In: A")

class B(A):
    def do_something(self):
        print("Method Define In B")

class C(A):
    def do_something(self):
        print("Method Defined In: C")

class D(B,C):
    def do_something(self):
        print("Method Defined in D:")


thing = D()
thing.do_something()


#print(D.__mro__)
#print(D.mro())
#help(D)