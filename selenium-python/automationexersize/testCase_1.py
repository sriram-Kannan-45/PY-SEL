from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def dismiss_ads(driver):
    try:
        driver.execute_script("""
            document.querySelectorAll('iframe').forEach(frame => {
                let src = frame.src || '';
                let id = frame.id || '';

                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads') ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift') ||
                    id.includes('google_ads')
                ) {
                    frame.remove();
                }
            });
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://automationexercise.com")

dismiss_ads(driver)

signup = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Signup / Login']")
    )
)
signup.click()

wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Name']")
    )
).send_keys("sriram")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='signup-email']"
).send_keys("sriramtitooo@gmail.com")

driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Signup']"
).click()

wait.until(
    EC.element_to_be_clickable(
        (By.ID, "id_gender1")
    )
).click()

driver.find_element(
    By.ID,
    "password"
).send_keys("sriram123@")

driver.find_element(
    By.ID,
    "first_name"
).send_keys("Sriram")

driver.find_element(
    By.ID,
    "last_name"
).send_keys("tioo")

driver.find_element(
    By.ID,
    "address1"
).send_keys("salem")

driver.find_element(
    By.ID,
    "state"
).send_keys("Tamilnadu")

driver.find_element(
    By.ID,
    "city"
).send_keys("salem")

driver.find_element(
    By.ID,
    "zipcode"
).send_keys("636008")

driver.find_element(
    By.ID,
    "mobile_number"
).send_keys("6381128745")

dismiss_ads(driver)

createbtn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-qa='create-account']")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    createbtn
)

driver.execute_script(
    "arguments[0].click();",
    createbtn
)

acccrea = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//b[normalize-space()='Account Created!']")
    )
).text

print(acccrea)

contbtn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@data-qa='continue-button']")
    )
)

driver.execute_script(
    "arguments[0].click();",
    contbtn
)

dismiss_ads(driver)

userName = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//a[contains(text(),'Logged in as')]")
    )
).text

print(userName)

if "Logged in as" in userName:
    print("The Logged username is show")
else:
    print("The logged username is not show")

delacc = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Delete Account']")
    )
)

if delacc.is_displayed():
    print("Delete button displayed")
else:
    print("Delete button not displayed")

driver.execute_script(
    "arguments[0].click();",
    delacc
)

deldisp = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//b[normalize-space()='Account Deleted!']")
    )
).text

print(deldisp)

delcont = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@data-qa='continue-button']")
    )
)

driver.execute_script(
    "arguments[0].click();",
    delcont
)

driver.quit()