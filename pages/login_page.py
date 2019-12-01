from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_page  = self.browser.current_url
        assert 'login' in login_page, "login is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL), "EMAIL field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD), "Password field is not presented"
        assert self.is_element_present(*LoginPageLocators.SUBMIT), "Submit button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "EMAIL field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD1), "Password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD2), "Password conformation field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_SUBMIT), "Submit button is not presented"