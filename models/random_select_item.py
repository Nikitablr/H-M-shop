import random
import re
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from locators.locators_main_page import MainPagelocators


#Выбираем рандомный товар из максимума товаров по категории
class RandomSelect():

    def __init__(self, browser):
        self.browser = browser
    def select_maximum(self):
        while True:
            try:
                item = self.browser.find_element(*MainPagelocators.MAXIMUM)
                digits_in_list = [float(s) for s in re.findall(r'-?\d+\.?\d*', item.text)]
                second_digit = digits_in_list[1]
                random_item = random.randint(1, int(second_digit))
                locator = str('//*[@id="page-content"]/div/div[3]/ul/li[' + str(random_item) + ']')
                self.browser.find_element(By.XPATH, locator).click()
                break
            except NoSuchElementException:
                self.browser.find_element(*MainPagelocators.LOAD_MORE_PRODUCTS_BUTTON).click()
                continue




