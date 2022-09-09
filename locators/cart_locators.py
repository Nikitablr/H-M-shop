from selenium.webdriver.common.by import By

class ProductPageLocators:
    PRODUCT_NAME = (By.XPATH, '//*[@id="js-product-name"]/div/h1')
    PRODUCT_COST = (By.XPATH, '//*[@id="product-price"]/div/span')
    ADD_TO_BAG_BUTTON = (By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/div[1]/div[1]/div/div[3]/button')
    PRODUCT_COLOR = (By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/h3')

class CartLocators:
    PRODUCT_NAME_IN_CART = (By.XPATH, '//*[@id="sidebar-sticky-boundary"]/section[1]/div/ul/li/article/div[1]/h2')
    PRODUCT_COST_IN_CART = (By.XPATH, '//*[@id="sidebar-sticky-boundary"]/section[1]/div/ul/li/article/div[1]/span')
    PRODUCT_COLOR_IN_CART = (By.XPATH, '//*[@id="sidebar-sticky-boundary"]/section[1]/div/ul/li/article/div[1]/ul/li[2]/span[2]')
    CONTINUE_TO_CHECKOUT_BUTTON = (By.XPATH, '//*[@id="sidebar-sticky-boundary"]/section[2]/div/div/div[1]/div[3]/button')
    REMOVE_FROM_CART_BUTTON = (By.XPATH, '//*[@id="sidebar-sticky-boundary"]/section[1]/div/ul/li[1]/article/button')