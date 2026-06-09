import pytest
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


@pytest.fixture()

def test_setup_and_teardown( request ):

    global driver

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield

    driver.quit()
