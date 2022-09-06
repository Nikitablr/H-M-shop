from pages.base_page import BasePage
from locators.locators_main_page import MainPagelocators

class MainPage(BasePage):

    def open_paris_trend_report_page(self):
        self.browser.find_element(*MainPagelocators.PARIS_TREND_REPORT_BUTTON)
        self.scroll_to_element(*MainPagelocators.PARIS_TREND_REPORT_BUTTON)
        self.click(*MainPagelocators.PARIS_TREND_REPORT_BUTTON)
        assert self.is_presented(*MainPagelocators.PARIS_TREND_REPORT_PAGE_IS_OPEN)

    def open_turn_up_the_color_page(self):
        self.browser.find_element(*MainPagelocators.TURN_UP_THE_COLOR_BUTTON)
        self.scroll_to_element(*MainPagelocators.TURN_UP_THE_COLOR_BUTTON)
        self.click(*MainPagelocators.TURN_UP_THE_COLOR_BUTTON)
        assert self.is_presented(*MainPagelocators.TURN_UP_THE_COLOR_PAGE_IS_OPEN)


