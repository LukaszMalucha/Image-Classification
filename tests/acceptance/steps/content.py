from behave import *
from pathlib import Path

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.digit_identifier_page import DigitIdentifierPage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.register_page import RegisterPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content

@then('There are three buttons shown on the page')
def step_impl(context):
    page = DigitIdentifierPage(context.driver)
    assert page.clear_button.is_displayed()
    assert page.download_button.is_displayed()
    assert page.predict_button.is_displayed()

@then('I can see there is a register form on the page')
def step_impl(context):
    page = RegisterPage(context.driver)
    assert page.form.is_displayed()


@then('I can see there is a login form on the page')
def step_impl(context):
    page = LoginPage(context.driver)
    assert page.form.is_displayed()

@then('I downloaded the image')
def step_impl(context):
    file = Path('C:\\Users\\MaximusMinimus\\Downloads\\digit.png')  ## specify
    assert file.exists()


@then('I can see there is the a prediction result on the page')
def step_impl(context):
    page = DigitIdentifierPage(context.driver)
    assert page.result.is_displayed()