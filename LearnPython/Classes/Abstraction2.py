from abc import ABC, abstractmethod

# this ia an abstract class which is unimplemented
class X(ABC):
    @abstractmethod
    def method1(self):
        pass
    @abstractmethod
    def method2(self):
        pass

# Method 1 is implemented in class Y
class Y(X):
    def method1(self):
        print("Method 1 is implemented")

# we cannot access method1 until we implement method 2 in class Y or any other class.
# Method 2 is implemented in class Z
class Z(Y):
    def method2(self):
        print("Method 2 is implemented")

obj = Z()
obj.method1()
obj.method2()