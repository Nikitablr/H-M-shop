from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.cart_page import CartPage



def test_add_product_to_favourite_page_from_view_all_on_women_page(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = MainPage(browser)
    page.open_view_all_on_women_page()
    page.open_random_product()
    page = CartPage(browser)
    page.add_to_favourite_page()
    page.check_add_to_favourite_page()

def test_add_product_to_favourite_page_from_view_all_on_men_page(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = MainPage(browser)
    page.open_view_all_on_men_page()
    page.open_random_product()
    page = CartPage(browser)
    page.add_to_favourite_page()
    page.check_add_to_favourite_page()

