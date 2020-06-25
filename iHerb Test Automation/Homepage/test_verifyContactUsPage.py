
# Verify Support Link opens Contact Us page
# 1. Go to iHerb and click on the 24/7 Support link
# 2. Veirfy link is working and user is redirected to a contact us  page
# 3. Go back to iHerb.com

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iherb.com/")
print(driver.title)

driver.find_element_by_xpath('//*[contains(text(), "Support")]').click()
print(driver.current_url)
driver.implicitly_wait(5)
driver.back()

driver.quit()
