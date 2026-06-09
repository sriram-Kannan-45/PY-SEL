import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import read_config


@pytest.fixture()
def test_setup_and_teardown():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")

    yield driver

    driver.quit()


def test_valproduct(test_setup_and_teardown):

    driver = test_setup_and_teardown

    val_item = read_config.get_config("search term", "val_item")

    driver.find_element(By.NAME, "search").send_keys(val_item, Keys.ENTER)

    assert driver.find_element(
        By.XPATH,
        '//a[text()="HP LP3065"]'
    ).is_displayed()


def test_invalproduct(test_setup_and_teardown):

    driver = test_setup_and_teardown

    inval_item = read_config.get_config("search term", "inVal_item")

    driver.find_element(By.NAME, "search").send_keys(inval_item, Keys.ENTER)

    actual = "There is no product that matches the search criteria."

    expected = driver.find_element(
        By.XPATH,
        '//p[contains(text(),"There is no product")]'
    ).text

    assert actual == expected


def test_noproduct(test_setup_and_teardown):


    print("noproduct")

    driver = test_setup_and_teardown

    driver.find_element(By.NAME, "search").send_keys("", Keys.ENTER)

    actual = "There is no product that matches the search criteria."

    expected = driver.find_element(
        By.XPATH,
        '//p[contains(text(),"There is no product")]'
    ).text

    assert actual == expected