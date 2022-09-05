from selenium.webdriver.common.by import By


class SearchLocators:

    SEARCH_FIELD = (By.XPATH, '//*[@id="main-search"]')
    NO_MATCHING_ITEMS_MESSAGE = (By.XPATH, '//*[@id="main-content"]/div[1]/h1')