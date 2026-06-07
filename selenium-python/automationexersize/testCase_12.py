from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def dismiss_ads(driver):
    try:
        driver.execute_script("""
            document.querySelectorAll(
                "iframe, .adsbygoogle, [id*='google_ads'], [id*='aswift']"
            ).forEach(el => el.remove());
        """)
        print("Ads removed")
    except Exception as e:
        print("No ads found:", e)


d = webdriver.Chrome()
wait = WebDriverWait(d, 10)

d.maximize_window()
d.get("https://automationexercise.com/")

dismiss_ads(d)
d.find_element(By.XPATH,"//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]").click()
dismiss_ads(d)
quantity=d.find_element(By.XPATH,"//input[@id='quantity']")
quantity.clear()
quantity.send_keys(4)
d.find_element(By.XPATH,"//button[@type='button']").click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//u[normalize-space()='View Cart']"))).click()
dismiss_ads(d)
UpdatedQuantity=wait.until(EC.visibility_of_element_located((By.XPATH,"//td[@class='cart_quantity']/button"))).text
assert UpdatedQuantity=='4'
print(UpdatedQuantity)