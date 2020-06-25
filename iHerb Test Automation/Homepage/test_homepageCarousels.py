"""
1. Go to www.iherb.com
2. Verify Trending Today Carousel. Return number of products
3. Verify Best Selling Carousel. Return Best Selling Country selection, selected tab and number of products
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        driver = self.driver
        driver.get('https://www.iherb.com/')

    def test_trending_carousel(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//b[contains(text(),'Trending Now')]")
            driver.find_element_by_xpath("//div[@class='filter-trending region-filter']//input["
                                         "@class='country-filter']")
            driver.find_element_by_id("trending-inner")
            product_inner = driver.find_elements_by_xpath("//div[@id='trending-inner']//div[@class='product']")

            trending_preview = []

            for i in product_inner:
                trending_preview.append(i)
            print('{} {}'.format(len(trending_preview), " products in Trending carousel ", ))

        except NoSuchElementException:
            print("No element found")

    def test_bestSelling_carousel(self):
        driver = self.driver

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Best Selling')]")))
        country = driver.find_element_by_xpath("//div[@class='filter-best-selling region-filter']"
                                               "//input[@class='country-filter']").get_attribute("value")
        activeBtn = driver.find_element_by_xpath("//button"
                                                 "[@class='btn best-selling-available-category-tab active']").text
        print('{} {} {} {}'.format("Best Selling is set to ", country, " and selected category is ", activeBtn))

        bestSelling = driver.find_elements_by_xpath("//div[@id='best-selling-inner']//div[@class='product-inner']")

        bestSellingProducts = []
        for products in bestSelling:
            bestSellingProducts.append(products)
        print('{} {} {} {}'.format(len(bestSellingProducts), " products in Best Selling ", activeBtn, " Category", ))

    def tearDown(self):
        self.driver.close()
