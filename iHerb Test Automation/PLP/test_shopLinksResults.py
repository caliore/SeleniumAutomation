"""
1. Open shop menu link
2 Verify PLP returns results
3. Print Pages Title and Number of results
"""

import unittest
import time
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

    def test_5htp(self):
        driver = self.driver
        driver.get('https://www.iherb.com/c/5-htp')
        driver.implicitly_wait(10)
        title = driver.find_element_by_class_name("sub-header-title").text
        result = driver.find_element_by_class_name("display-items").text
        print(title + " " + result)

    def test_algae(self):
        driver = self.driver
        driver.get('https://www.iherb.com/c/algae')
        driver.implicitly_wait(10)
        title = driver.find_element_by_class_name("sub-header-title").text
        result = driver.find_element_by_class_name("display-items").text
        print(title + " " + result)

    def test_aloeVera(self):
        driver = self.driver
        driver.get('https://www.iherb.com/c/aloe-vera')
        driver.implicitly_wait(10)
        title = driver.find_element_by_class_name("sub-header-title").text
        result = driver.find_element_by_class_name("display-items").text
        print(title + " " + result)

    def test_aminoAcids(self):
        driver = self.driver
        driver.get('https://www.iherb.com/c/amino-acids')
        driver.implicitly_wait(10)
        title = driver.find_element_by_class_name("sub-header-title").text
        result = driver.find_element_by_class_name("display-items").text
        print(title + " " + result)

    def test_antioxidants(self):
        driver = self.driver
        driver.get('https://www.iherb.com/c/antioxidants')
        driver.implicitly_wait(10)
        title = driver.find_element_by_class_name("sub-header-title").text
        result = driver.find_element_by_class_name("display-items").text
        print(title + " " + result)

    def test_ashwagandha(self):
        driver = self.driver
        driver.get('https://www.iherb.com/c/ashwagandha')
        driver.implicitly_wait(10)
        title = driver.find_element_by_class_name("sub-header-title").text
        result = driver.find_element_by_class_name("display-items").text
        print(title + " " + result)

    def test_Astaxanthin(self):
        driver = self.driver
        driver.get('https://www.iherb.com/c/astaxanthin')
        driver.implicitly_wait(10)
        title = driver.find_element_by_class_name("sub-header-title").text
        result = driver.find_element_by_class_name("display-items").text
        print(title + " " + result)

    def test_propolis(self):
        driver = self.driver
        driver.get('https://www.iherb.com/c/Propolis')
        driver.implicitly_wait(10)
        title = driver.find_element_by_class_name("sub-header-title").text
        result = driver.find_element_by_class_name("display-items").text
        print(title + " " + result)

    def tearDown(self):
        self.driver.close()
