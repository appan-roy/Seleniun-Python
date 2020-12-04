import pytest

# IMPORTANT : All the python files and methods must starts with test / end with test

@pytest.mark.home
def test_addition():
    x = 10
    y = 7
    assert x+y == 17, "Addition is wrong"
    
def test_subtraction():
    x = 10
    y = 7
    assert x-y == 3, "Subtraction is wrong"

@pytest.mark.login
def test_login_instagram():
    assert "admin" == "admin123", "Invalid credential"