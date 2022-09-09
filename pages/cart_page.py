from pages.base_page import BasePage
from locators.cart_locators import *


class CartPage(BasePage):

    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BAG_BUTTON)
        button.click()