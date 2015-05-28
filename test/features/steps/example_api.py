from behave import *
import requests,json

@when('I make a call')
def step_impl(context):
    response = requests.get('https://api.github.com/users/jaimegildesagredo/repos')
    assert response.status_code == 200
    print(response.content)

@then('I print response')
def step_impl(context):
    print("inside then")