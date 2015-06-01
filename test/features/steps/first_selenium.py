from behave import *
from selenium import webdriver

@given('I open seleniumframework website')
def step_impl(context):
   context.browser.get("http://www.seleniumframework.com")

@then('I print the title')
def step_impl(context):
   title = context.browser.title
   assert "Selenium" in title


@then("I print domain")
def step_impl(context):
    print(context.browser.current_url)