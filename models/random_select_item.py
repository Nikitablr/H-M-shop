from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import random
from locators.locators_main_page import MainPagelocators
from pages.base_page import BasePage
import re
from selenium.webdriver.common.action_chains import ActionChains

class RandomSelect(BasePage):

    def select_maximum(self):
        while True:
            try:
                item = BasePage.find_element(*MainPagelocators.MAXIMUM)
                digits_in_list = [float(s) for s in re.findall(r'-?\d+\.?\d*', item.text)]
                second_digit = digits_in_list[1]
                random_item = random.randint(1, int(second_digit))
                locator = str('//*[@id="page-content"]/div/div[3]/ul/li[' + str(random_item) + ']')
                self.browser.find_element(By.XPATH, locator).click()
                break
            except NoSuchElementException:
                self.browser.find_element(*MainPagelocators.LOAD_MORE_PRODUCTS_BUTTON).click()
                continue




