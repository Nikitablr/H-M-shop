from locators.signin_locators import SigninLocators
from pages.base_page import BasePage
from locators.locators_search import SearchLocators
from models.search_faker import SearchData


class SearchPage(BasePage):

    def open_search_page(self):
        self.click(*SigninLocators.ACCEPT_ALL_COOKIES_BUTTON)
        search_button = self.browser.find_element(*SearchLocators.SEARCH_FIELD)
        search_button.click()

    def entering_a_search_term(self):
        request = self.browser.find_element(*SearchLocators.SEARCH_FIELD)
        request.send_keys('T-shirt')
        request.submit()
        assert 'shirt' in self.browser.title

    def entering_no_matching_search_request(self):
        data = SearchData.random()
        request = self.browser.find_element(*SearchLocators.SEARCH_FIELD)
        request.send_keys(data.text)
        request.submit()
        assert self.is_presented(*SearchLocators.NO_MATCHING_ITEMS_MESSAGE)


