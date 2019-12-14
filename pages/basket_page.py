from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_see_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are basket items, should not be"
        lang = self.get_current_language()
        text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        if lang == 'en':
            assert text == "Your basket is empty. Continue shopping", f"Excepted 'Your basket is empty',got {text}"
        elif lang == 'ru':
            assert text == "Ваша корзина пуста Продолжить покупки", f"Excepted 'Ваша корзина пуста',got {text}"


