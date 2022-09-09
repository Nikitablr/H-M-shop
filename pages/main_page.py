from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from locators.locators_main_page import *
import re
import random
from selenium.webdriver.common.by import By

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

    def open_view_all_page(self):
        self.click(*MainPagelocators.WOMEN_BUTTON)
        self.click(*MainPagelocators.VIEW_ALL_BUTTON)

    def open_random_product(self):
        while True:
            try:
                item = self.browser.find_element(*MainPagelocators.MAXIMUM)
                digits_in_list = [float(s) for s in re.findall(r'-?\d+\.?\d*', item.text)]
                second_digit = digits_in_list[1]
                random_item = random.randint(1, int(second_digit))
                locator = str('//*[@id="page-content"]/div/div[3]/ul/li[' + str(random_item) + ']')
                self.click(By.XPATH, locator)
                break
            except NoSuchElementException:
                self.browser.find_element(*MainPagelocators.LOAD_MORE_PRODUCTS_BUTTON).click()
                continue



