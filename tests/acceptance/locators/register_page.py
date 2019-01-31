from selenium.webdriver.common.by import By


class RegisterPageLocators:
    REGISTER_FORM = By.ID, 'form-signin'
    USERNAME_FIELD = By.ID, 'username'
    EMAIL_FIELD = By.ID, 'email'
    PASSWORD = By.ID, 'password'
    SUBMIT_BUTTON = By.ID, 'submit-button'
