from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.wait import WebDriverWait 



driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver , 10 )

driver.get("https://www.leafground.com/drag.xhtml;jsessionid=node0zaiqw3ht84l9u4dtb5y5jaf817677175.node0")

button1 = driver.find_element(By.XPATH , '//p[text()="Drag to target"]')

tarButton = driver.find_element(By.XPATH , '//p[text()="Drop here"]')

actions = ActionChains(driver)

actions.click_and_hold(button1).move_to_element(tarButton).release().perform()



