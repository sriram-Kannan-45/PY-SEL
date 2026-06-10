from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SearchProduct(BasePage):

    searchBar = '//input[@placeholder="Search"]'

    def searchProducts(self, product):

        search = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.searchBar))
        )

        search.clear()
        search.send_keys(product)
        search.send_keys(Keys.ENTER)