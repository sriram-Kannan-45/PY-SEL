from selenium import webdriver

import time

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://automationexercise.com/")

homePage = "https://automationexercise.com/"

# driver.implicitly_wait(10)

if driver.current_url == homePage :

    print ("Verifide home page")

    

    testCasePage = driver.find_element(By.XPATH , '//a[text()=" Test Cases"]')

    testCasePage.click()

    
    
    testCaseText = driver.find_element(By.XPATH,"//b[contains(text(),'Test Cases')]")

    if testCaseText.is_displayed():

        print("testCase page verified")

    else :

        print ("testcase page not verified")

else :

    print ("not Verify home page")