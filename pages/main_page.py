from pages.base_page import BasePage
from locators.locators_main_page import *
from models.random_select_item import RandomSelect


class MainPage(BasePage):

    #Открыть страницу 'Trend report page'
    def open_paris_trend_report_page(self):
        self.browser.find_element(*MainPagelocators.PARIS_TREND_REPORT_BUTTON)
        self.scroll_to_element(*MainPagelocators.PARIS_TREND_REPORT_BUTTON)
        self.click(*MainPagelocators.PARIS_TREND_REPORT_BUTTON)
        assert self.is_presented(*MainPagelocators.PARIS_TREND_REPORT_PAGE_IS_OPEN)

    #Открыть страницу 'Turn up the color'
    def open_turn_up_the_color_page(self):
        self.browser.find_element(*MainPagelocators.TURN_UP_THE_COLOR_BUTTON)
        self.scroll_to_element(*MainPagelocators.TURN_UP_THE_COLOR_BUTTON)
        self.click(*MainPagelocators.TURN_UP_THE_COLOR_BUTTON)
        assert self.is_presented(*MainPagelocators.TURN_UP_THE_COLOR_PAGE_IS_OPEN)

    #Открыть страницу 'View all' во вкладке Women
    def open_view_all_on_women_page(self):
        self.click(*MainPagelocators.WOMEN_BUTTON)
        self.click(*MainPagelocators.VIEW_ALL_BUTTON)

    #Открываем рандомный товар на странице 'View all' во вкладке 'Women'
    def open_random_product(self):
        RandomSelect.select_maximum(self)

    def open_view_all_on_men_page(self):
        self.click(*MainPagelocators.MEN_BUTTON)
        self.click(*MainPagelocators.VIEW_ALL_BUTTON)














