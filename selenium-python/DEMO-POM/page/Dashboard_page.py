from page.base_page import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):

    my_account_assert = '//h2[text()="My Account"]'

    def verify_login(self, expected):

        actual = self.driver.find_element(
            By.XPATH,
            self.my_account_assert
        ).text

        assert actual == expected