from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/")

driver.maximize_window()

time.sleep(3)

element = driver.find_element(By.XPATH, '//a[@target="_blank"]')

scroll_origin = ScrollOrigin.from_element(element)

ActionChains(driver)\
    .scroll_from_origin(scroll_origin, 0, 500)\
    .perform()

time.sleep(12)