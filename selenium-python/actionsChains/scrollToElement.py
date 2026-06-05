from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/")

driver.maximize_window()

time.sleep(10) 

element = driver.find_element(By.XPATH, "//h5[contains(text(),'Book')]")

ActionChains(driver).scroll_to_element(element).perform()

time.sleep(10)