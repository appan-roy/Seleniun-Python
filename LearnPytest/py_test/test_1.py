import pytest

# IMPORTANT : All the python files and methods must starts with test / end with test

@pytest.mark.home
def test_equal_numbers():
    a = 5
    b = 5
    assert a == b, "a is not equals to b"

def test_equal_strings():
    str1 = "APPAN"
    str2 = "appan"
    assert str1.lower() == str2, "Strings are not equal"

@pytest.mark.login
def test_login_gmail():
    assert "admin" == "admin", "Invalid credential"