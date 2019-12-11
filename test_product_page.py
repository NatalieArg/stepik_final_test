from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import faker


class TestGuestAddToBasketFromProductPage:
    @pytest.mark.parametrize('page_param', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
    def test_guest_can_add_product_to_basket(self, browser, page_param):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{page_param}"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_product_to_basket()
        page.solve_quiz_and_get_code()  # вводим код
        page.should_see_message_add_to_basket()  # проверяем что есть сообщение о добавлении товара в корзину
        page.should_see_price_of_product()


    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_product_to_basket()
        page.should_not_be_message_add_product_to_basket()


    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_message_add_product_to_basket()


    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_product_to_basket()
        page.should_disappear_message_add_product_to_basket()


    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()  # проверяем что открылась страница регистрации с нужными полями


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_go_to_basket()
        basket_page.should_see_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        f = faker.Faker()
        email = f.email()
        password = f.password()
        new_reg = LoginPage(browser, link)
        new_reg.open()
        new_reg.register_new_user(email, password)
        new_reg.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_message_add_product_to_basket()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_product_to_basket()
        page.should_see_message_add_to_basket()  # проверяем что есть сообщение о добавлении товара в корзину
        page.should_see_price_of_product()
