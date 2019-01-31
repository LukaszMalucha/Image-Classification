from selenium.webdriver.common.by import By

from tests.acceptance.locators.digit_identifier_page import DigitIdentifierPageLocators
from tests.acceptance.page_model.base_page import BasePage


class DigitIdentifierPage(BasePage):
    @property
    def url(self):
        return super(DigitIdentifierPage, self).url + '/digit_recognition'


    @property
    def title(self):
        return self.driver.find_element(*DigitIdentifierPageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*DigitIdentifierPageLocators.NAV_LINKS)

    @property
    def dropdown(self):
        return self.driver.find_element(*DigitIdentifierPageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*DigitIdentifierPageLocators.DROPDOWN_LINKS)

    @property
    def clear_button(self):
        return self.driver.find_element(*DigitIdentifierPageLocators.CLEAR_BUTTON)

    @property
    def download_button(self):
        return self.driver.find_element(*DigitIdentifierPageLocators.DOWNLOAD_BUTTON)

    @property
    def predict_button(self):
        return self.driver.find_element(*DigitIdentifierPageLocators.PREDICT_BUTTON)

    @property
    def result(self):
        return self.driver.find_element(*DigitIdentifierPageLocators.RESULT)
