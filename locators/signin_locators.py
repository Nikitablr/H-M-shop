from selenium.webdriver.common.by import By


class SigninLocators:
    SIGNIN_PAGE_BUTTON = (By.XPATH, '/html/body/header/nav/ul[1]/li[1]/div')
    EMAIL_FIELD = (By.ID, 'modal-txt-signin-email')
    PASSWORD_FIELD = (By.ID,'modal-txt-signin-password')
    SIGNIN_BUTTON = (By.ID, 'modal-theLoginForm')
    ACCEPT_ALL_COOKIES_BUTTON = (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
