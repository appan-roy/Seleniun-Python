import unittest


class SignupTest(unittest.TestCase):

    def test_signupByGoogle(self):
        print("This is a signup test using Google account")
        self.assertTrue(True)

    def test_signupByFacebook(self):
        print("This is a signup test using Facebook account")
        self.assertTrue(True)
        
    def test_signupByTwitter(self):
        print("This is a signup test using Twitter account")
        self.assertTrue(True)

# the below block is used to run as python-run
if __name__ == "__main__":
    unittest.main()