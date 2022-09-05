from selenium.webdriver.common.by import By


class SignupLocators:
    BECOME_A_MEMBER_BUTTON = (By.XPATH, '/html/body/div[13]/div/div/button')
    EMAIL_FIELD = (By.ID, 'modal-signin-email')
    CREATE_A_PASSWORD_FIELD = (By.ID,'modal-signin-password')
    DATE_FIELD = (By.XPATH, '//*[@id="modal-signin-day"]')
    MONTH_FIELD = (By.XPATH, '//*[@id="modal-signin-month"]')
    YEAR_FIELD = (By.XPATH, '//*[@id="modal-signin-year"]')
    CONFIRM_EMAIL_FIELD = (By.ID, 'forgottenPwd.email')
    SUBMIT_BUTTON = (By.CLASS_NAME, 'button')
    MESSAGE_AFTER_SIGNUP = (By.ID, 'main-content')
    SIGNUP_BUTTON = (By.XPATH, '/html/body/div[14]/div/div/div/form/button')
