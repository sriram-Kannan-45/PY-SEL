from tkinter.tix import TEXT

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WAIT
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demoqa.com/browser-windows")

wait = WAIT(driver , 10)

parent_window = driver.current_window_handle

wait.until(EC.element_to_be_clickable((By.XPATH , '//button[text()="New Window"]'))).click()

allWindows = driver.window_handles

for win in allWindows :

    if win != parent_window :

        driver.switch_to.window(win)

        break
    


txt = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//h1'))
).text


print(txt)