from abc import ABC, abstractmethod

# this ia an abstract class which is unimplemented
class Abs(ABC):
    # constructor
    def __init__(self, value):
        self.value = value
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass

# myClass implements the abstract methods of abstract class Abs
class myClass(Abs):
    def add(self):
        print(self.value + 10)
    def sub(self):
        print(self.value - 10)

obj = myClass(100)  # sets self.value = 100 in Abs class
obj.add()   # 110
obj.sub()   # 90