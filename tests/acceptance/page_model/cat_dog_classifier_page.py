from selenium.webdriver.common.by import By

from tests.acceptance.locators.cat_dog_classifier_page import CatDogClassifierPageLocators
from tests.acceptance.page_model.base_page import BasePage


class CatDogClassifierPage(BasePage):
    @property
    def url(self):
        return super(CatDogClassifierPage, self).url + '/classifier'


    @property
    def title(self):
        return self.driver.find_element(*CatDogClassifierPageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*CatDogClassifierPageLocators.NAV_LINKS)

    @property
    def dropdown(self):
        return self.driver.find_element(*CatDogClassifierPageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*CatDogClassifierPageLocators.DROPDOWN_LINKS)


