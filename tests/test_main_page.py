from pages.header_main_page import HeaderMainPage
from pages.base_page import BasePage

def test_jump_to_pages(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = HeaderMainPage(browser)
    page.open_women_page()
    page.open_divided_page()
    page.open_men_page()
    page.open_baby_page()
    page.open_kids_page()
    page.open_home_page()
    page.open_sport_page()
    page.open_sale_page()
    page.open_sustainability_page()