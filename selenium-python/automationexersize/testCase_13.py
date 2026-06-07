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

# Add first product
product1 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")
    )
)
d.execute_script("arguments[0].click();", product1)
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class,'close-modal')]")
    )
).click()

dismiss_ads(d)

product2 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//a[contains(text(),'Add to cart')])[3]")
    )
)
d.execute_script("arguments[0].click();", product2)

view_cart = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//u[normalize-space()='View Cart']")
    )
)
view_cart.click()

dismiss_ads(d)
table = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//table[@id='cart_info_table']")
    )
)
print(table.text)
assert table.text!=""
d.quit()