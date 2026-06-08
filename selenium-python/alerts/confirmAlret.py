from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demoqa.com/alerts?utm_source=chatgpt.com")

driver.find_element(By.XPATH , '//button[@id = "confirmButton"]').click()

alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)

print(alert.text)

alert.accept()

driver.quit()