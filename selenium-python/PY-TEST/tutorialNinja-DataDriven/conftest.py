import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from util import config_read as read


@pytest.fixture()
def test_setup_and_down(request):


    browser = read.get_config("browser and url" , "browser")
    url = read.get_config("browser and url" , "url")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.Firefox()


    
    driver.maximize_window()
    
    driver.get(url)

    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)

    yield driver

    driver.quit()