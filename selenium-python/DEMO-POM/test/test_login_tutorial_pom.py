import pytest
from selenium import webdriver

from page.Home_page import LoginPage
from page.Dashboard_page import DashboardPage

from utilities import config_reader as read


@pytest.mark.usefixtures("test_setup_and_down")
class TestLogin:

    def test_valid_login(self):

        login_page = LoginPage(self.driver)

        email = read.get_config("userEmail and password" , "email")
        password  = read.get_config("userEmail and password" , "password")

        login_page.login(
        email,
        password
        )

        dashboard = DashboardPage(self.driver)
        dashboard.verify_login("My Account")