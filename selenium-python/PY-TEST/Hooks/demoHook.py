from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def setup_function(function):
    global driver

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")


def teardown_function(function):
    driver.quit()


def test_valproduct():

    driver.find_element(
        By.NAME,
        "search"
    ).send_keys("HP", Keys.ENTER)

    assert driver.find_element(
        By.XPATH,
        '//a[text()="HP LP3065"]'
    ).is_displayed()