from selenium import webdriver

def before_all(context):
    print("Executing before all")

def before_feature(context, feature):
    print("Before feature")

def before_scenario(context,scenario):
    context.browser = webdriver.Chrome()

def after_scenario(context,scenario):
    context.browser.quit()

def after_feature(context,feature):
    print("After feature")

def after_all(context):
    print("Executing after all")

