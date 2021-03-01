import unittest


def setUpModule():
    print("This is setup module")
    
def tearDownModule():
    print("This is teardown module")
    
class firstClass(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("This is setup class 1")
    
    @classmethod
    def tearDownClass(cls):
        print("This is teardown class 1")
        
    def setUp(self):
        print("This is setup method class 1")
        
    def tearDown(self):
        print("This is teardown method class 1")
        
    def test_case1(self):
        print("This is class 1 test 1")
        
    def test_case2(self):
        print("This is class 1 test 2")
        
    def test_case3(self):
        print("This is class 1 test 3")

class secondClass(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("This is setup class 2")
    
    @classmethod
    def tearDownClass(cls):
        print("This is teardown class 2")
        
    def setUp(self):
        print("This is setup method class 2")
        
    def tearDown(self):
        print("This is teardown method class 2")
        
    def test_case1(self):
        print("This is class 2 test 1")
        
    def test_case2(self):
        print("This is class 2 test 2")
        
    def test_case3(self):
        print("This is class 2 test 3")
                
# the below block is used to run as python-run
if __name__ == "__main__":
    unittest.main()