from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://demoqa.com/alerts")

button = driver.find_element(
    By.ID,
    "timerAlertButton"
)

driver.execute_script("arguments[0].click();", button)

alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)

print(alert.text)

alert.accept()

driver.quit()