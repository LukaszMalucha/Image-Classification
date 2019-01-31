from selenium.webdriver.common.by import By


class DigitIdentifierPageLocators:
    TITLE = By.ID, 'page_title'
    NAV_LINKS =  By.ID, 'navigation'
    DROPDOWN = By.ID, 'user_dropdown'
    DROPDOWN_LINKS = By.ID, 'dropdown_link'
    PAGE = By.ID, 'page-index'
    CLEAR_BUTTON = By.ID, 'clear'
    DOWNLOAD_BUTTON = By.ID, 'download'
    PREDICT_BUTTON = By.ID, 'predict'
    RESULT = By.ID, 'predict'

