# Exception Handling: 
# try block - the code which may cause exception
# except block - will run if there is an exception occurs
# else block - will run if there is no exception occurs
# finally block - will run always at the end irrespective of occurence of exceptions
try:
    num1 = int(input("Please enter first number : "))
    num2 = int(input("Please enter second number : "))
    quotient = num1 / num2
    print("Result is : ", quotient)
except TypeError as err:
    print("Please check the below error message:-\n", err)
except ValueError as err:
    print("Please check the below error message:-\n", err)
except ZeroDivisionError as err:
    print("Please check the below error message:-\n", err)
except Exception as err:
    print("Please check the below error message:-\n", err)
else:
    print("There is no exception")
finally:
    print("The operation is done")