from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://thinking-tester-contact-list.herokuapp.com/")

driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys("wavene2@gmail.com")
driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys("sriram123@")
driver.find_element(By.XPATH, '//button[text()="Submit"]').click()

wait = WebDriverWait(driver, 10)

rows = wait.until(
    EC.visibility_of_all_elements_located(
        (By.XPATH, "//table//tr")
    )
)

for i in rows :

   if "Sriram" in i.text :
      
      print(i.text)

driver.quit()