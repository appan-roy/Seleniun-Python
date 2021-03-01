import unittest


class LoginTest(unittest.TestCase):

    def test_loginByGoogle(self):
        print("This is a login test using Google account")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("This is a login test using Facebook account")
        self.assertTrue(True)
        
    def test_loginByTwitter(self):
        print("This is a login test using Twitter account")
        self.assertTrue(True)

# the below block is used to run as python-run
if __name__ == "__main__":
    unittest.main()