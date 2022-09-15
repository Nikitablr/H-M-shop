from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.main_page import MainPage

def test_add_random_product_to_cart(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = MainPage(browser)
    page.open_view_all_on_women_page()
    page.open_random_product()
    page = CartPage(browser)
    page.select_size()
    page.add_product_to_cart()
    page.open_cart_page_in_new_window()

