from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_BAG_BUTTON = (By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/div[1]/div[1]/div/div[3]/button')
    SELECT_SIZE = (By.XPATH, '//*[@id="picker-1"]/button')
    ITEM_IN_STOCK = (By.CSS_SELECTOR, "li[class='item  js-enable-nib']")
    CART_PAGE_BUTTON = (By.XPATH, '/html/body/header/nav/ul[1]/li[4]/span/a')
    FAVOURITE_BUTTON = (By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/div[1]/div[1]/div/hm-favourites-button/button')
    FAVOURITE_PAGE = (By.XPATH, '/html/body/header/nav/ul[1]/li[2]/button')

class FavouriteLocators:
    PRODUCT_NAME_ON_FAVOURITE_PAGE = (By.XPATH, '//*[@id="main-content"]/div[2]/ul[1]/li/article/div[2]/div/h2/a')
    PRODUCT_NAME_ON_PAGE = (By.XPATH,'//*[@id="js-product-name"]/div/h1')
