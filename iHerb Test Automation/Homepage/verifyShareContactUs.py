
# Verify Support Link opens Contact Us page
# 1. Go to iHerb and print Title
# 2. Verify share link is clickable and 24/7 link is working and user is redirected to a contact us  page
# 3. Go back to iHerb.com

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iherb.com/")
print(driver.title)

driver.find_element_by_xpath('//div[@class="iherb-header-share share-page"]').click()
wait = WebDriverWait(driver, 5)
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='share-notice row']")))

driver.find_element_by_xpath('//*[contains(text(), "Support")]').click()
print(driver.current_url)
driver.implicitly_wait(5)
driver.back()


driver.quit()
