__author__ = 'pmacharl'

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        self.driver.get("http://www.practiceselenium.com/practice-form.html")
        assert "practice-form" in self.driver.title
        first_name = self.driver.find_element_by_name("firstname")
        first_name.send_keys("Pradeep")
        self.driver.find_element_by_name("lastname").send_keys("Kumar")
        self.driver.find_element_by_id("sex-1").click()
        self.driver.find_element_by_id("exp-3").click()
        self.driver.find_element_by_id("datepicker").send_keys("1/1/2001")
        self.driver.find_element_by_id("tea1").click()
        self.driver.find_element_by_id("tool-0").click()
        Select(self.driver.find_element_by_id("continents")).select_by_visible_text("Europe")
        Select(self.driver.find_element_by_id("selenium_commands")).select_by_visible_text("Navigation Commands")
        self.driver.find_element_by_id("submit").click()
        assert "Welcome" in self.driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
