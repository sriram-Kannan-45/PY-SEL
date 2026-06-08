import pytest
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("test_setup_and_teardown")

class TestSearch :

    def test_valproduct( self):

        self.driver.find_element(By.NAME , 'search').send_keys("HP" , Keys.ENTER )

        assert self.driver.find_element(By.XPATH , '//a[text()="HP LP3065"]').is_displayed() 

    
    def test_invalproduct( self ):

        self.driver.find_element(By.NAME , 'search').send_keys("honda" , Keys.ENTER )

        actual = "There is no product that matches the search criteria."

        expect = self.driver.find_element(By.XPATH , '//p[contains(text() , "no")]').text

        assert actual == expect

    
    def test_noproduct ( self ):

        self.driver.find_element(By.NAME , 'search').send_keys("" , Keys.ENTER )

        actual = "There is no product that matches the search criteria."

        expect = self.driver.find_element(By.XPATH , '//p[contains(text() , "no")]').text

        assert actual == expect