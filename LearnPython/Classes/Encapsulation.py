class myClass:
    a = 10  # public variable
    __empid = 101    # private variable

    def method1(self):
        print("This is a public method")    # public method
    
    def __method2(self):
        print("This is a private method")  # private method

    def set_emp_id(self, eid):              # public method to manipulate private variable
        self.__empid = eid

    def get_emp_id(self):               # public method to show private variable
        print(self.__empid)

# create class object
obj = myClass()

# access public var and method
print(obj.a)
obj.method1()

# update private variable
obj.set_emp_id(201)

# access private variable
obj.get_emp_id()