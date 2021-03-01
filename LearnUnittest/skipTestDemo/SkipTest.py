import unittest


class SkippingTests(unittest.TestCase):

    def test_case_1(self):
        print("This is test case 1")

    @unittest.skip("This test case is not ready yet")
    def test_case_2(self):
        print("This is test case 2")
    
    def test_case_3(self):
        print("This is test case 3")

    @unittest.skipIf(5 == 3+2, "This test can't be run on equal numbers") 
    def test_case_4(self):
        print("This is test case 4")
        
    def test_case_5(self):
        print("This is test case 5")
    
    @unittest.skipUnless(5 != 3+2, "This test can't be run on unequal numbers")  
    def test_case_6(self):
        print("This is test case 6")

# the below block is used to run as python-run
if __name__ == "__main__":
    unittest.main()