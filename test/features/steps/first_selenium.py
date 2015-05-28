from behave import *
from selenium import webdriver

@given('I open seleniumframework website')
def step_impl(context):
   print("inside given step")
   global driver
   driver = webdriver.Chrome()
   driver.get("http://www.seleniumframework.com")

@then('I print the title')
def step_impl(context):
   title = driver.title
   assert "Selenium" in title
   driver.close