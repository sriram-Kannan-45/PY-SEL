import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.parametrize(
    "search_term",
    ["selenium", "pytest", "locators"]
)
def test_google_search(search_term):

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.google.com/")

    driver.find_element(
        By.XPATH,
        '//textarea[@id="APjFqb"]'
    ).send_keys(search_term, Keys.ENTER)

    time.sleep(2)
    driver.quit()