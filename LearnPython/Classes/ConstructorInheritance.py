class classA:
    def __init__(self):
        print("Hello from class A")

class classB(classA):
    def __init__(self):
        super().__init__()  # class A constructor will be invoked
        print("Hello from class B")

class classC(classB):
    def __init__(self):
        super().__init__()  # class B constructor will be invoked
        print("Hello from class C")

# class C constructor will be invoked once we create the object of class C
c = classC()    # Hello from class A, Hello from class B, Hello from class C