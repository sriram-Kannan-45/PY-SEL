import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.mark.parametrize("browser", ["c", "e"])
@pytest.mark.parametrize(
    "url",
    [
        "https://www.flipkart.com/",
        "https://www.google.com/search?q=www.amazon.com+india"
    ]
)
def test_url(browser, url):

    if browser == "c":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

    elif browser == "e":
        options = EdgeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)

    driver.get(url)

    print(f"{browser} ---------------------------- {driver.title}")

    driver.quit()