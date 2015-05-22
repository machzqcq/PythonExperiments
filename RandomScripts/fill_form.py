__author__ = 'pmacharl'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://www.practiceselenium.com/practice-form.html")
assert "practice-form" in driver.title

first_name = driver.find_element_by_name("firstname")
first_name.send_keys("Pradeep")
driver.find_element_by_name("lastname").send_keys("Kumar")
driver.find_element_by_id("sex-1").click()
driver.find_element_by_id("exp-3").click()
driver.find_element_by_id("datepicker").send_keys("1/1/2001")
driver.find_element_by_id("tea1").click()
driver.find_element_by_id("tool-0").click()
Select(driver.find_element_by_id("continents")).select_by_visible_text("Europe")
Select(driver.find_element_by_id("selenium_commands")).select_by_visible_text("Navigation Commands")
driver.find_element_by_id("submit").click()

assert "Welcome" in driver.title

driver.quit()