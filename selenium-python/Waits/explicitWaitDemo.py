from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';

                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads') ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift') ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")


driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://automationexercise.com/")

if "automationexercise.com" in driver.current_url:

    print("Verified Home Page")

    dismiss_ads(driver)

    test_case_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/test_cases')]")))

    test_case_menu.click()

    test_case_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2/b[contains(text(),'Test Cases')]")
        )
    )

    if test_case_text.is_displayed():
        print("Test Cases Page Verified")
    else:
        print("Test Cases Page Not Verified")

else:
    print("Home Page Not Verified")

driver.quit()