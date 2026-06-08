


import time

from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/select.xhtml;jsessionid=node0mnszv12jr098fcvenwq17eoy17900206.node0")

dropDown = Select(driver.find_element(By.XPATH , '//select[@class="ui-selectonemenu"]'))


for option in dropDown.options:

    if option.text == "Playwright":

        option.click()
        break

    
time.sleep(12)


