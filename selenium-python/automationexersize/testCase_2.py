from selenium import webdriver

import time

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://automationexercise.com/")

homePage = "https://automationexercise.com/"

if driver.current_url == homePage :

    print ("Verify home page")

    loginBtn = driver.find_element(
    By.XPATH,
    '//a[text()=" Signup / Login"]'
    
    )

    loginBtn.click()

    driver.find_element(
        By.XPATH , '//input[@data-qa="login-email"]'
    ).send_keys("titooram123@gmail.com")

    driver.find_element(By.XPATH , '//input[@type="password"]').send_keys("sriram123@")

    driver.find_element(By.XPATH , '//button[text()="Login"]').click()

    logInMsg  = driver.find_element(By.XPATH , '//a[text()=" Logged in as "]')

    if (logInMsg.is_displayed) :

        print("login successFull")

    else :

        print("login unsuccessFull")


else :

    print ("verification failed")

driver.quit()

