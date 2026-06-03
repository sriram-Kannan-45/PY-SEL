from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.google.com/")
print("Google Title:", driver.title)

time.sleep(3)

driver.get("https://www.amazon.in")
print("Amazon Title:", driver.title)

time.sleep(3)

driver.back()
time.sleep(3)
print("After Back:", driver.title)

driver.forward()
time.sleep(3)
print("After Forward:", driver.title)

driver.refresh()
time.sleep(3)
print("After Refresh:", driver.title)

driver.quit()