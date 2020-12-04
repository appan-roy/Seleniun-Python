class classA:
    def hello(self):
        print("Hello from class A")

class classB(classA):
    def hello(self):
        print("Hello from class B")

class classC(classB):
    def hello(self):
        classB.hello(self)  # to access hello() from class B in spite of method overriding
        print("Hello from class C")

class classD(classC):
    def hello(self):
        super().hello()     # to access hello() from class C in spite of method overriding
        print("Hello from class D")

b = classB()
b.hello()       # Hello from class B - method overriding

c = classC()
c.hello()       # Hello from class B, Hello from class C

d = classD()
d.hello()       # Hello from class B, Hello from class C, Hello from class D