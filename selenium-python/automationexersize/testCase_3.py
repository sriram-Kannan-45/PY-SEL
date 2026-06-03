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

    driver.find_element(By.XPATH , '//input[@type="password"]').send_keys("sriram1")

    driver.find_element(By.XPATH , '//button[text()="Login"]').click()


    error = driver.find_element(By.XPATH , '//p[text()="Your email or password is incorrect!"]')

    if error.is_displayed() :

        print("error handled with the invalid credentials")

    else :

        print("error not handled with the invalid credentials")

else :

    print ("verification failed")

driver.quit()

