from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

# frame=driver.find_element(By.XPATH,"//iframe[@id='iframe1']")

driver.switch_to.frame(1)

iframeTxt = driver.find_element(By.XPATH,"//a[normalize-space()='What is Selenium?']").text

print(iframeTxt)

driver.switch_to.default_content()

driver.quit()