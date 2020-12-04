import pytest

@pytest.mark.usefixtures("init_driver")    
class BaseTest():
    pass


class Test_Orange_HRM(BaseTest):
    
    @pytest.mark.parametrize(
        "username, password",
            [
                ("Admin", "admin123"),
                ("Admin1", "admin123"),
                ("Admin2", "admin123")
            ]
        )
    def test_login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == "OrangeHRM"
        self.driver.find_element_by_id("txtUsername").send_keys(username)
        self.driver.find_element_by_id("txtPassword").send_keys(password)
        