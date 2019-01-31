from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS =  By.ID, 'navigation'
    DROPDOWN = By.ID, 'user_dropdown'
    DROPDOWN_LINKS = By.ID, 'dropdown_link'
    PAGE = By.ID, 'page-index'
    DIGIT_RECOGNITION_LINK = By.ID, 'digit_recognition_link'
    CLASSIFY_IMAGE_LINK = By.ID, 'classify_image_link'
    CAT_DOG_CLASSIFIER_LINK = By.ID, 'cat_dog_classifier_link'
