# Method 1
""" import MyModule

MyModule.hello_world()
MyModule.bank_loan_emi() """

# Method 2 
""" from MyModule import hello_world
from MyModule import bank_loan_emi

hello_world()
bank_loan_emi() """

# Method 3
""" from MyModule import hello_world, bank_loan_emi

hello_world()
bank_loan_emi() """

# Method 4
from MyModule import *

hello_world()
bank_loan_emi()