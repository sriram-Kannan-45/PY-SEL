from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.maximize_window()
driver.get("https://www.leafground.com/select.xhtml")

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//button[@aria-label="Show Options"]')
    )
).click()

# items_to_select = ["Selenium WebDriver", "Appium"]

dropDownList = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, '//span/ul/li')
    )
)

for option in dropDownList:

    if option.text == "Appium" or option.text == "Selenium WebDriver" :

        option.click()

driver.quit()