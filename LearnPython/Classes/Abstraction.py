from abc import ABC, abstractmethod

# this ia an abstract class which is unimplemented
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

# the abstract class Animal is implemented in its subclass Tiger
class Tiger(Animal):
    def eat(self):
        print("Eats NON-VEG")

# the abstract class Animal is implemented in its subclass Cow
class Cow(Animal):
    def eat(self):
        print("Eats VEG")

t = Tiger()
t.eat()

c = Cow()
c.eat()