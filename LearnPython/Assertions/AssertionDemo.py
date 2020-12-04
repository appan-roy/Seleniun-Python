import math

# example 1
assert "Selenium" in "Selenium if for Web Automation", "Selenium is not present"
print("Validation 1 passed")

# example 2
assert "Python" == "Python", "Strings did not match"
print("Validation 2 passed")

# example 3
assert "Python" in ["Java", "JavaScript", "Python"], "Python is not present"
print("Validation 3 passed")

# example 4
assert math.sqrt(4) == 2, "Value is wrong"
print("Validation 4 passed")