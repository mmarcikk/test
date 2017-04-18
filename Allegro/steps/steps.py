from behave import *
import time
from page_objects import XPATH_OBJECTS
from nose import tools as assertions


@given('the page "{url}" is loaded')
def step_impl(context, url):
    context.browser.get(url)
    time.sleep(1)


@when('I type "{text}" in "{input_id}" input')
def step_impl(context, text, input_id):
    input_field = context.browser.find_element_by_xpath(XPATH_OBJECTS['input_id'].format(input_id=input_id))
    input_field.send_keys(text)
    time.sleep(1)


@when('I click button with value "{button_value}"')
def step_impl(context, button_value):
    context.browser.find_element_by_xpath(XPATH_OBJECTS['button_value'].format(button_value=button_value)).click()
    time.sleep(1)


@then('the result page is displayed with "{value}"')
def step_impl(context, value):
    value_on_page = context.browser.find_element_by_xpath(XPATH_OBJECTS['displayed_text'].format(value=value)).text
    assertions.assert_equal(value, value_on_page)


@when('I click on podkategoria "{value}"')
def step_impl(context, value):
    context.browser.find_element_by_xpath(XPATH_OBJECTS['displayed_text'].format(value=value)).click()
    time.sleep(1)


@when('I select "{value}" from wojewodztwo dropdown')
def step_impl(context, value):
    location = context.browser.find_element_by_xpath(XPATH_OBJECTS['location_dropdown'].format(value=value))
    location.click()
    time.sleep(1)


@then('delete location option is available')
def step_impl(context):
    context.browser.find_element_by_xpath(XPATH_OBJECTS['delete_location'])
