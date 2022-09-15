from pages.base_page import BasePage
from locators.cart_locators import *


class CartPage(BasePage):

    def select_size(self):
        self.scroll_to_element(*ProductPageLocators.SELECT_SIZE)
        self.click(*ProductPageLocators.SELECT_SIZE)
        self.scroll_to_element(*ProductPageLocators.ITEM_IN_STOCK)
        self.click(*ProductPageLocators.ITEM_IN_STOCK)

    def add_product_to_cart(self):
        self.scroll_to_element(*ProductPageLocators.ADD_TO_BAG_BUTTON)
        self.click(*ProductPageLocators.ADD_TO_BAG_BUTTON)

    def open_cart_page(self):
        self.click(*ProductPageLocators.CART_PAGE_BUTTON)

    def open_cart_page_in_new_window(self):
        self.click(*ProductPageLocators.CART_PAGE_BUTTON)
        self.switch_to_new_window(1)



