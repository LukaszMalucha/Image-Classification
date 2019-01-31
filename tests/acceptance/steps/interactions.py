from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.digit_identifier_page import DigitIdentifierPage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.register_page import RegisterPage


use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text]
    matching_links[0].click()

@when('I click on the dropdown menu')
def step_impl(context):
    page = BasePage(context.driver)
    page.dropdown.click()

@when('I click on the "(.*)" dropdown link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.dropdown_links
    matching_links = [l for l in links if l.text == link_text]
    matching_links[0].click()

@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = RegisterPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I enter "(.*)" in the "(.*)" login field')
def step_impl(context, content, field_name):
    page = LoginPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I choose "(.*)" field')
def step_impl(context, field_name):
    page = BasePage(context.driver)
    page.form_field(field_name).click()


@when('I press the submit button')
def step_impl(context):
    page = RegisterPage(context.driver)
    page.submit_button.click()


@when('I press the login button')
def step_impl(context):
    page = LoginPage(context.driver)
    page.submit_button.click()


@when('I press the download button')
def step_impl(context):
    page = DigitIdentifierPage(context.driver)
    page.download_button.click()


@when('I press the predict button')
def step_impl(context):
    page = DigitIdentifierPage(context.driver)
    page.predict_button.click()


@when('I click the digit recognition link')
def step_impl(context):
    page = DigitIdentifierPage(context.driver)
    page.digit_recognition_link.click()

@when('I click the classify image link')
def step_impl(context):
    page = DigitIdentifierPage(context.driver)
    page.classify_image_link.click()

@when('I click the cat dog classifier link')
def step_impl(context):
    page = DigitIdentifierPage(context.driver)
    page.cat_dog_classifier_link.click()
