from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")
    EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")