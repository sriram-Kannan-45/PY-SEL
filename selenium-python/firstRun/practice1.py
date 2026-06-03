from selenium import webdriver

import time

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.google.com/")
print("Google Title:", driver.title)

enable = driver.find_element(By.NAME , value='q').is_enabled()

if enable :

    print("enable")

else :

    print("not enable")

driver.find_element(By.NAME, "q").send_keys("selenium")

time.sleep(2)

enableBtn = driver.find_element(By.XPATH , "//div[@class='T14B5e iThwld']/child::center/child::input[1]" ) 

if enableBtn.is_enabled() :

    enableBtn.click()

    time.sleep(10)

driver.quit()