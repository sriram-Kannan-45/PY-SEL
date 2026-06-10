from test.BaseTest import TestLoginBase
from page.searchPage import SearchProduct
from page.product_page import ProductPage


class TestSearch(TestLoginBase):

    def test_search(self):

        
        self.login()

        
        search = SearchProduct(self.driver)
        search.searchProducts("HP")

        
        product = ProductPage(self.driver)
        product.assertProduct("HP")

        print("done")