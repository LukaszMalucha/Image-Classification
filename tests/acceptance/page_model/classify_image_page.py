from tests.acceptance.locators.classify_image_page import ClassifyImagePageLocators
from tests.acceptance.page_model.base_page import BasePage


class ClassifyImagePage(BasePage):
    @property
    def url(self):
        return super(ClassifyImagePage, self).url + '/classify'


    @property
    def title(self):
        return self.driver.find_element(*ClassifyImagePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*ClassifyImagePageLocators.NAV_LINKS)

    @property
    def dropdown(self):
        return self.driver.find_element(*ClassifyImagePageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*ClassifyImagePageLocators.DROPDOWN_LINKS)
