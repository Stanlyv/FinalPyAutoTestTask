from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_NOTIFICATION), "Basket IS NOT empty"

    def should_basket_not_empty(self):
        assert not self.browser.find_element(*BasketPageLocators.EMPTY_NOTIFICATION), "Basket IS empty"
