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

    def should_see_message_add_to_basket(self):
        self.name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        self.name_in_basket_book = self.name_in_basket.text
        assert self.name_book == self.name_in_basket_book, f"Expected {self.name_book}, got {self.name_in_basket_book}, Name of product in the basket is not correct"

    def should_see_price_of_product(self):
        self.price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        self.price_in_basket_book = self.price_in_basket.text
        assert self.price_book == self.price_in_basket_book, f"Expected {self.price_book}, got {self.price_in_basket_book}, Price of product in the basket is not correct"

    def should_not_be_message_add_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
            "Product name added to basket is presented, but should not be"
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET), \
            "Product price added to basket is presented, but should not be"

    def should_disappear_message_add_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
            "Product name added to basket should disappear, but did not"
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET), \
            "Product price added to basket should disappear, but did not"