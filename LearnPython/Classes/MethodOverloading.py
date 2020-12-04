class Bird:
    def fly(self, name = None):
        if name == "Parrot":    print("Can fly")
        elif name == "Penguine":    print("Can't fly")
        elif name == None:  print("No input")

obj = Bird()
obj.fly("Parrot")
obj.fly("Penguine")
obj.fly()