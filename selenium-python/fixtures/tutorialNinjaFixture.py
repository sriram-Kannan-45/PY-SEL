import pytest
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


@pytest.fixture()

def test_setup_and_teardown():

    global driver

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    yield

    driver.quit()

def test_valproduct( test_setup_and_teardown ):

    driver.find_element(By.NAME , 'search').send_keys("HP" , Keys.ENTER )

    assert driver.find_element(By.XPATH , '//a[text()="HP LP3065"]').is_displayed() 

    
def test_invalproduct( test_setup_and_teardown ):

    driver.find_element(By.NAME , 'search').send_keys("honda" , Keys.ENTER )

    actual = "There is no product that matches the search criteria."

    expect = driver.find_element(By.XPATH , '//p[contains(text() , "no")]').text

    assert actual == expect

    
def test_noproduct ( test_setup_and_teardown ):

    driver.find_element(By.NAME , 'search').send_keys("" , Keys.ENTER )

    actual = "There is no product that matches the search criteria."

    expect = driver.find_element(By.XPATH , '//p[contains(text() , "no")]').text

    assert actual == expect