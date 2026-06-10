from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    my_account = '//a[@title="My Account"]'
    login_link = '//a[text()="Login"]'
    user_email = '//input[@placeholder="E-Mail Address"]'
    user_pass = '//input[@placeholder="Password"]'
    submit = '//input[@type="submit"]'

    error = '//div[contains(text(),"Warning")]'

    def login(self, email, password):

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.my_account))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.login_link))
        ).click()

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.user_email))
        ).send_keys(email)

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.user_pass))
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.submit))
        ).click()

    def assertError(self, expected):

        actual = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.error))
        ).text

        assert expected in actual