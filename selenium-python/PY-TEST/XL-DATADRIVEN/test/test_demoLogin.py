
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import excelReader
import utilities.logCreater as logCreater


logger = logCreater.log_generator()


@pytest.mark.parametrize(
    "username,password",
    excelReader.get_data(
        "ExcelFiles/loginData.xlsx",
        "loginData"
    )
)
def test_ValLogin(username, password):

    logger.info("========== Login Test Started ==========")

    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    try:

        driver.get("https://www.demoblaze.com/index.html")
        logger.info("Application launched successfully")

        wait.until(
            EC.element_to_be_clickable((By.ID, "login2"))
        ).click()

        logger.info("Login popup opened")

        wait.until(
            EC.visibility_of_element_located((By.ID, "loginusername"))
        ).send_keys(username)

        logger.info(f"Username entered: {username}")

        wait.until(
            EC.visibility_of_element_located((By.ID, "loginpassword"))
        ).send_keys(password)

        logger.info("Password entered")

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))
        ).click()

        logger.info("Login button clicked")

        logout = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[text()='Log out']"))
        ).text

        assert logout == "Log out", "Login Failed"

        logger.info("Login successful")

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Log out']"))
        ).click()

        logger.info("Logout successful")

    except Exception as e:

        logger.error(f"Test Failed : {e}")

        raise

    finally:

        driver.quit()

        logger.info("Browser closed")
        logger.info("========== Login Test Completed ==========")

