

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import read_util as read

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def test_setup_and_teardown():

   
    browser = read.get_config("Basic info","browser")

    if browser == 'chrome' :

        driver = webdriver.Chrome()

    elif browser == 'edge' :

        driver = webdriver.Edge()

    url = read.get_config("Basic info","url")

    driver.get(url)

    driver.maximize_window()

    wait = WebDriverWait(driver , 10)

    yield driver

    driver.quit()

def test_ValLogin(test_setup_and_teardown):

    driver = test_setup_and_teardown

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[@id="login2"]'))
    ).click()

    name = read.get_config("Login info", "userName")
    passWord = read.get_config("Login info", "userPass")

    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//input[@id="loginusername"]'))
    ).send_keys(name)

    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//input[@id="loginpassword"]'))
    ).send_keys(passWord)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in"]'))
    ).click()

    logout = wait.until(EC.visibility_of_element_located((By.XPATH , '//a[text()="Log out"]'))).text

    assert logout == "Log out"

    print("Login completed")

def test_inValLogin(test_setup_and_teardown):

    driver = test_setup_and_teardown

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[@id="login2"]'))
    ).click()

    name = read.get_config("Login info", "invaluserName")
    passWord = read.get_config("Login info", "invaluserPass")

    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//input[@id="loginusername"]'))
    ).send_keys(name)

    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//input[@id="loginpassword"]'))
    ).send_keys(passWord)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in"]'))
    ).click()

    alert = wait.until(EC.alert_is_present())

    print(alert.text)

    print(alert.accept())

    print("Login completed")