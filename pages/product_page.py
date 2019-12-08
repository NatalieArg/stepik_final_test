from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        self.name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        self.name_book = self.name.text
        self.price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        self.price_book = self.price.text
        add_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)  # добавляем в корзину
        add_button.click()
        self.solve_quiz_and_get_code()  # вводим код
        self.should_see_message_add_to_basket()  # проверяем что есть сообщение о добавлении товара в корзину
        self.should_see_price_of_product()  # проверяем что отображается нужная цена

    def should_see_message_add_to_basket(self):
        self.name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        self.name_in_basket_book = self.name_in_basket.text
        assert self.name_book == self.name_in_basket_book, f"Expected {self.name_book}, got {self.name_in_basket_book}, Name of product in the basket is not correct"


    def should_see_price_of_product(self):
        self.price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        self.price_in_basket_book = self.price_in_basket.text
        assert self.price_book == self.price_in_basket_book, f"Expected {self.price_book}, got {self.price_in_basket_book}, Price of product in the basket is not correct"

