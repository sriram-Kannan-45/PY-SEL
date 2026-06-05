from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/")

driver.maximize_window()

time.sleep(5)


ActionChains(driver).scroll_by_amount(0, 1000).perform()

time.sleep(10)

driver.quit()