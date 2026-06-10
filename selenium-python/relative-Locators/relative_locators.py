
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

textarea = driver.find_element(By.NAME, "my-textarea")

textbox = driver.find_element(
    locate_with(By.NAME, "my-text").above(textarea)
)

textbox.send_keys("Sriram")



name = driver.find_element(By.XPATH , '//label[contains(text(),"Text input")]')

pw = driver.find_element(
    locate_with(By.NAME , 'my-password').below(name))

pw.send_keys("sriram123@")



dropdown = driver.find_element(By.XPATH , '//label[contains(text(),"(select)")]')

default_radio = driver.find_element(By.ID, "my-radio-2")

checked_radio = driver.find_element(
    locate_with(By.CSS_SELECTOR, "input[type='radio']")
    .to_left_of(default_radio)
)

checked_radio.click()
time.sleep(2)