from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    productText = '//a[contains(text(),"HP")]'

    def assertProduct(self, expected):

        actual = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.productText)
            )
        ).text

        assert expected in actual