from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def dropdown(self):
        return self.driver.find_element(*BasePageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*BasePageLocators.DROPDOWN_LINKS)

    @property
    def classify_image_link(self):
        return self.driver.find_element(*BasePageLocators.CLASSIFY_IMAGE_LINK)

    @property
    def cat_dog_classifier_link(self):
        return self.driver.find_element(*BasePageLocators.CAT_DOG_CLASSIFIER_LINK)

    @property
    def digit_recognition_link(self):
        return self.driver.find_element(*BasePageLocators.DIGIT_RECOGNITION_LINK)























