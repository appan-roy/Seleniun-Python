class Base:
    name = "Appan"
    def base_method(self):
        print("I am in base method")

class Child(Base):
    age = 30
    def child_method(self):
        print("I am in child method")

# accessing base class variable ans method using base class object
b = Base()
print(b.name)
b.base_method()

# accessing child class variable ans method using child class object
c = Child()
print(c.age)
c.child_method()

# accessing base class variable ans method using child class object
print(c.name)
c.base_method()