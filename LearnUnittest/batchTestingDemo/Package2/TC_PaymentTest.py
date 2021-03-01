import unittest


class PaymentTest(unittest.TestCase):

    def test_paymentByCash(self):
        print("This is a payment test by cash")
        self.assertTrue(True)

    def test_paymentByCheque(self):
        print("This is a payment test by cheque")
        self.assertTrue(True)
        
    def test_paymentByNEFT(self):
        print("This is a payment test by NEFT")
        self.assertTrue(True)

# the below block is used to run as python-run
if __name__ == "__main__":
    unittest.main()