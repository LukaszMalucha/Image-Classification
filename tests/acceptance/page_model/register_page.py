from selenium.webdriver.common.by import By

from tests.acceptance.locators.register_page import RegisterPageLocators
from tests.acceptance.page_model.base_page import BasePage


class RegisterPage(BasePage):
    @property
    def url(self):
        return super(RegisterPage, self).url + '/register'

    @property
    def form(self):
        return self.driver.find_element(*RegisterPageLocators.REGISTER_FORM)

    @property
    def submit_button(self):
        return self.driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)
