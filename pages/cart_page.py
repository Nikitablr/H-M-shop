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

    def add_to_favourite_page(self):
        self.click(*ProductPageLocators.FAVOURITE_BUTTON)

    def check_add_to_favourite_page(self):
        self.browser.switch_to.new_window('window')
        favourite_page_url = 'https://www2.hm.com/en_us/favourites'
        self.browser.get(favourite_page_url)
        name_on_favourite_page = self.browser.find_element(*FavouriteLocators.PRODUCT_NAME_ON_FAVOURITE_PAGE).text
        self.browser.switch_to.window(self.browser.window_handles[0])
        name_on_page = self.browser.find_element(*FavouriteLocators.PRODUCT_NAME_ON_PAGE).text
        assert name_on_page == name_on_favourite_page



