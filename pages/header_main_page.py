from pages.base_page import BasePage
from locators.locators_main_page import MainPagelocators

class HeaderMainPage(BasePage):

    #Открываем страницу Women page в хедере
    def open_women_page(self):
        page = self.browser.find_element(*MainPagelocators.WOMEN_BUTTON)
        page.click()
        assert 'Women' in self.browser.title

    #Открываем страницу Divided page в хедере
    def open_divided_page(self):
        page = self.browser.find_element(*MainPagelocators.DIVIDED_BUTTON)
        page.click()
        assert 'Divided' in self.browser.title

    #Открываем страницу Men page в хедере
    def open_men_page(self):
        page = self.browser.find_element(*MainPagelocators.MEN_BUTTON)
        page.click()
        assert 'Men' in self.browser.title

    #Открываем страницу Baby page в хедере
    def open_baby_page(self):
        page = self.browser.find_element(*MainPagelocators.BABY_BUTTON)
        page.click()
        assert 'Baby' in self.browser.title

    #Открываем страницу Kids page в хедере
    def open_kids_page(self):
        page = self.browser.find_element(*MainPagelocators.KIDS_BUTTON)
        page.click()
        assert 'Kids' in self.browser.title

    #Открываем страницу Home page в хедере
    def open_home_page(self):
        page = self.browser.find_element(*MainPagelocators.H_M_HOME_BUTTON)
        page.click()
        assert 'Home' in self.browser.title

    #Открываем страницу Sport page в хедере
    def open_sport_page(self):
        page = self.browser.find_element(*MainPagelocators.SPORT_BUTTON)
        page.click()
        assert 'Sportswear' in self.browser.title

    #Открываем страницу Sale page в хедере
    def open_sale_page(self):
        page = self.browser.find_element(*MainPagelocators.SALE_BUTTON)
        page.click()
        assert 'sale' in self.browser.title

    #Открываем страницу Sale page в хедере
    def open_sustainability_page(self):
        page = self.browser.find_element(*MainPagelocators.SUSTAINABILITY_BUTTON)
        page.click()
        assert 'Sustainability' in self.browser.title





