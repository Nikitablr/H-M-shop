from selenium.webdriver.common.by import By


class MainPagelocators:
    WOMEN_BUTTON = (By.XPATH, '/html/body/header/nav/ul[2]/li[2]/a')
    DIVIDED_BUTTON = (By.XPATH, '/html/body/header/nav/ul[2]/li[3]/a')
    MEN_BUTTON = (By.XPATH, '/html/body/header/nav/ul[2]/li[4]/a')
    BABY_BUTTON = (By.XPATH, '/html/body/header/nav/ul[2]/li[5]/a')
    KIDS_BUTTON = (By.XPATH, '/html/body/header/nav/ul[2]/li[6]/a')
    H_M_HOME_BUTTON = (By.XPATH, '/html/body/header/nav/ul[2]/li[7]/a')
    SPORT_BUTTON = (By.XPATH, '/html/body/header/nav/ul[2]/li[8]/a')
    SALE_BUTTON = (By.XPATH, '/html/body/header/nav/ul[2]/li[9]/a')
    SUSTAINABILITY_BUTTON = (By.XPATH, '/html/body/header/nav/ul[2]/li[10]/a')