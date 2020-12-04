# MRO - Method Resolution Order is the order in which Python looks for a method in a hierarchy of classes
class classA:
    def method_A(self):
        print("I am in class A")
    def hello(self):
        print("Hello from class A")

class classB():
    def method_B(self):
        print("I am in class B")
    def hello(self):
        print("Hello from class B")

class classC(classA, classB):
    def method_C(self):
        print("I am in class C")

c = classC()
c.method_A()
c.method_B()
c.method_C()
c.hello()   # here class A hello method will be called because of MRO
print(classC.mro())     # [<class '__main__.classC'>, <class '__main__.classA'>, <class '__main__.classB'>, <class 'object'>]