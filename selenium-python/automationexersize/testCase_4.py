from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")
signup = driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']")
signup.click()
name = driver.find_element(By.XPATH,"//input[@placeholder='Name']").send_keys("sriram")
email = driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("sriram@gmail.com")
signupbtn = driver.find_element(By.XPATH,"//button[normalize-space()='Signup']").click()
errmsg = driver.find_element(By.XPATH,"//p[text()='Email Address already exist!']").text
strmsg="Email Address already exist!"
assert strmsg == errmsg,"Message not shown"