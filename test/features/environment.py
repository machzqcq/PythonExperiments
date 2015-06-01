from selenium import webdriver

def before_all(context):
     print("Executing before all")

def before_feature(context, feature):
     print("Before feature\n")

def before_scenario(context,scenario):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()

def after_scenario(context,scenario):
    context.browser.quit()

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):
     print("Executing after all")

