import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def test_setup_and_teardown():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")

    yield driver

    driver.quit()


@pytest.mark.order(1)
def test_valproduct(test_setup_and_teardown):

    print("val")

    driver = test_setup_and_teardown

    driver.find_element(By.NAME, "search").send_keys("HP", Keys.ENTER)

    assert driver.find_element(
        By.XPATH,
        '//a[text()="HP LP3065"]'
    ).is_displayed()


@pytest.mark.order(3)
def test_invalproduct(test_setup_and_teardown):

    print("inval")

    driver = test_setup_and_teardown

    driver.find_element(By.NAME, "search").send_keys("Honda", Keys.ENTER)

    actual = "There is no product that matches the search criteria."

    expected = driver.find_element(
        By.XPATH,
        '//p[contains(text(),"There is no product")]'
    ).text

    assert actual == expected


@pytest.mark.order(2)
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