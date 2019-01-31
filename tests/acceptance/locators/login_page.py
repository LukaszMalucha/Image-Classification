from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = By.ID, 'login-form'
    USERNAME_FIELD = By.ID, 'username'
    PASSWORD = By.ID, 'password'
    SUBMIT_BUTTON = By.ID, 'submit-button'