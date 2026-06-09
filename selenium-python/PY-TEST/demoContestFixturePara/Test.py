import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_up_and_down")
class Test:
    def test_validproduct(self):
        self.driver.find_element(By.NAME, value="search").send_keys("HP")
        self.driver.find_element(
            By.XPATH, value="//button[contains(@class,'btn-default')]"
        ).click()
        assert self.driver.find_element(By.LINK_TEXT, value="HP LP3065").is_displayed()

    def test_invalidproduct(self):
        self.driver.find_element(By.NAME, value="search").send_keys("Honda")
        self.driver.find_element(
            By.XPATH, value="//button[contains(@class,'btn-default')]"
        ).click()
        etext = "There is no product that matches the search criteria."
        assert self.driver.find_element(
            By.XPATH, value="//input[@id='button-search']/following-sibling::p"
        ).text.__eq__(etext)

    def test_noproduct(self):
        self.driver.find_element(By.NAME, value="search").send_keys("")
        self.driver.find_element(
            By.XPATH, value="//button[contains(@class,'btn-default')]"
        ).click()
        etext = "There is no product that matches the search criteria."
        assert self.driver.find_element(
            By.XPATH, value="//input[@id='button-search']/following-sibling::p"
        ).text.__eq__(etext)