from pages.search_page import SearchPage
from pages.base_page import BasePage


def test_search_result(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = SearchPage(browser)
    page.open_search_page()
    page.entering_a_search_term()

def test_no_matching_search_request(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = SearchPage(browser)
    page.open_search_page()
    page.entering_no_matching_search_request()