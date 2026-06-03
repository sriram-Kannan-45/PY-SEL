import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://www.google.com/")

string = driver.title

print(string)

driver.close