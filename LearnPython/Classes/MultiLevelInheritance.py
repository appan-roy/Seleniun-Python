class classA:
    def method_A(self):
        print("I am in class A")
    def hello(self):
        print("Hello from class A")

class classB(classA):
    def method_B(self):
        print("I am in class B")
    def hello(self):
        print("Hello from class B")

class classC(classB):
    def method_C(self):
        print("I am in class C")
    def hello(self):
        print("Hello from class C")

c = classC()
c.method_A()
c.method_B()
c.method_C()
c.hello()   # here class C hello method will be called as this method overrides the hello method of class B and A respectively