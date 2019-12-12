from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import faker

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

class TestGuestAddToBasketFromProductPage:
    @pytest.mark.parametrize('page_param', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
    def test_guest_can_add_product_to_basket_promo(self, browser, page_param):
        linkn = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{page_param}"
        page = ProductPage(browser, linkn)
        page.open()  # открываем страницу
        page.should_add_product_to_basket()  # добавляем товар в корзину
        page.solve_quiz_and_get_code()  # вводим код
        page.should_see_message_add_to_basket()  # проверяем что есть сообщение о добавлении товара в корзину
        page.should_see_price_of_product()  # проверяем что есть цена в корзине

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_add_product_to_basket()  # добавляем товар в корзину
        page.should_see_message_add_to_basket()  # проверяем что есть сообщение о добавлении товара в корзину
        page.should_see_price_of_product()  # проверяем что есть цена в корзине

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()  #  открываем страницу
        page.should_add_product_to_basket()  # добавляем товар в корзину
        page.should_not_be_message_add_product_to_basket()  # проверяем что нет сообщения о добавлении товара в корзину

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу товара
        page.should_not_be_message_add_product_to_basket()  # проверяем что нет сообщения о добавлении в корзину

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_add_product_to_basket()  # добавляем товар в корзину
        page.should_disappear_message_add_product_to_basket()  # проверяем что исчезает сообщение о добавлении товара

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_be_login_link()  # проверяем что есть ссылка на страницу регистрации

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # передаем текущий url в объект нового класса
        login_page.should_be_login_page()  # проверяем что открылась страница регистрации с нужными полями

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_go_to_basket()   # переходим в корзину
        basket_page.should_see_empty_basket()  # проверяем что корзина пуста


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        linkn = "http://selenium1py.pythonanywhere.com/accounts/login/"
        f = faker.Faker()
        email = f.email()  # генерируем тестовый email
        password = f.password()  # генерируем тестовы пароль
        new_reg = LoginPage(browser, linkn)
        new_reg.open()  # открываем страницу
        new_reg.register_new_user(email, password)  # регистрируем нового пользователя
        new_reg.should_be_authorized_user()  # проверяем что пользователь авторизован

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_not_be_message_add_product_to_basket()  # проверяем что нет сообщения о добавлении в корзину

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.should_add_product_to_basket()  # добавляем товар в корзину
        page.should_see_message_add_to_basket()  # проверяем что есть сообщение о добавлении товара в корзину
        page.should_see_price_of_product()  # проверяем что есть цена товара в корзине
