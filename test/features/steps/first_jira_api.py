from behave import *
import requests,json

use_step_matcher("re")


@when("I query jira")
def step_impl(context):
    response = requests.get('http://PCW7MCHIPOLET1.inmar.com:8083/jira/rest/api/2/search?jql=assignee=pmacharl',auth=('admin','Inmar2015'))
    assert response.status_code == 200
    print(response.text)


@then('I list all issues for "pmacharl"')
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass