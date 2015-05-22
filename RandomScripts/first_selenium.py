__author__ = 'pmacharl'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.seleniumframework.com")
print(driver.title)
assert "Selenium Framework | Selenium, Cucumber, Ruby, Java et al." in driver.title
elem = driver.find_element_by_link_text("ABOUT")
elem.click()
assert "Pradeep K. Macharla" in driver.page_source
driver.close()