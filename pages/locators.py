from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


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


class ProductPageLocators:
    ADD_PRODUCT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")

class BasketPageLocators:
    GO_BASKET = (By.CSS_SELECTOR, ".btn-group a[href$='/basket/']")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
