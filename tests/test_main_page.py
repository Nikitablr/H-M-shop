from pages.header_main_page import HeaderMainPage
from pages.base_page import BasePage
from pages.main_page import MainPage

def test_go_to_pages_in_header(browser):
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

def test_go_to_paris_trend_report_page(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = MainPage(browser)
    page.open_paris_trend_report_page()

def test_go_to_turn_up_the_color_page(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = MainPage(browser)
    page.open_turn_up_the_color_page()










