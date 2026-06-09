import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox", "edge"])
def test_up_and_down(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()