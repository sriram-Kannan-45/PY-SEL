import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from util import excelUtil
from util.logger import log_generator

logger = log_generator()

@pytest.mark.usefixtures("test_setup_and_down")
class TestLogin:

    @pytest.mark.parametrize(
        "username,password",
        excelUtil.get_data(
            "ExcelData/data.xlsx",
            "Sheet1"
        )
    )
    def test_vallogin(self, username, password):

        logger.info("Starting Login Test")
        logger.info(f"Username : {username}")

        self.driver.find_element(By.LINK_TEXT, "My Account").click()

        self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        ).click()

        self.driver.find_element(
            By.XPATH,
            '//input[@placeholder="E-Mail Address"]'
        ).send_keys(username)

        self.driver.find_element(
            By.XPATH,
            '//input[@placeholder="Password"]'
        ).send_keys(password)

        self.driver.find_element(
            By.XPATH,
            '//input[@value="Login"]'
        ).click()

        heading = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//h2[text()="My Account"]')
            )
        )

        assert heading.text == "My Account"

        logger.info("Login Successful")


    @pytest.mark.parametrize(
        "username,password",
        excelUtil.get_data(
            "ExcelData/data.xlsx",
            "Sheet2"
        )
    )
    def test_inVallogin(self, username, password):

        logger.info("Starting Login Test")
        logger.info(f"Username : {username}")

        self.driver.find_element(By.LINK_TEXT, "My Account").click()

        self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        ).click()

        self.driver.find_element(
            By.XPATH,
            '//input[@placeholder="E-Mail Address"]'
        ).send_keys(username)

        self.driver.find_element(
            By.XPATH,
            '//input[@placeholder="Password"]'
        ).send_keys(password)

        self.driver.find_element(
            By.XPATH,
            '//input[@value="Login"]'
        ).click()

        error = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[contains(text(),"Warning")]')
            )
        )

        assert "Warning" in error.text

        logger.info("error")