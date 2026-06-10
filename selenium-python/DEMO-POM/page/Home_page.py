from page.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    my_account = '//a[@title="My Account"]'
    login_link = '//a[text()="Login"]'
    user_email = '//input[@placeholder="E-Mail Address"]'
    user_pass = '//input[@placeholder="Password"]'
    submit = '//input[@type="submit"]'

    def login(self, email, password):

        self.driver.find_element(By.XPATH, self.my_account).click()
        self.driver.find_element(By.XPATH, self.login_link).click()
        self.driver.find_element(By.XPATH, self.user_email).send_keys(email)
        self.driver.find_element(By.XPATH, self.user_pass).send_keys(password)
        self.driver.find_element(By.XPATH, self.submit).click()