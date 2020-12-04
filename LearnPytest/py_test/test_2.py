import pytest

# IMPORTANT : All the python files and methods must starts with test / end with test

@pytest.mark.login
def test_login_facebook():
    assert "admin" == "admin", "Invalid credential"

@pytest.mark.home
def test_assertTrue():
    assert True

def test_assertFalse():
    assert False