import unittest
from batchTestingDemo.Package1.TC_LoginTest import LoginTest
from batchTestingDemo.Package1.TC_SignupTest import SignupTest
from batchTestingDemo.Package2.TC_PaymentTest import PaymentTest


# get all the tests from LoginTest, SignupTest and PaymentTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

# create test suites
sanityTestSuite = unittest.TestSuite([tc1, tc3])
regressionTestSuite = unittest.TestSuite([tc2, tc3])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3])

# define suite runner
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)