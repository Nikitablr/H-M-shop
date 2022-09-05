from pages.base_page import BasePage
from locators.signup_locators import SignupLocators
from locators.signin_locators import SigninLocators
from models.signin_signup_faker import SignupData


class SignupPage(BasePage):

    def open_signup_page(self):
        self.click(*SigninLocators.ACCEPT_ALL_COOKIES_BUTTON)
        self.hover_to_element(*SigninLocators.SIGNIN_PAGE_BUTTON)
        self.click(*SigninLocators.SIGNIN_PAGE_BUTTON)
        self.wait_to_be_clickable(SignupLocators.BECOME_A_MEMBER_BUTTON)


    def fill_fields_for_signup(self):
        data = SignupData.random()
        self.fill(data.email, *SignupLocators.EMAIL_FIELD)
        self.fill(data.password, *SignupLocators.CREATE_A_PASSWORD_FIELD)
        self.fill(data.date, *SignupLocators.DATE_FIELD)
        self.fill(data.month, *SignupLocators.MONTH_FIELD)
        self.fill(data.year, *SignupLocators.YEAR_FIELD)
        self.scroll_to_element(*SignupLocators.SIGNUP_BUTTON)
        self.click(*SignupLocators.SIGNUP_BUTTON)
        self.fill(data.confirm_email, *SignupLocators.CONFIRM_EMAIL_FIELD)
        self.click(*SignupLocators.SUBMIT_BUTTON)
        assert self.is_presented(*SignupLocators.MESSAGE_AFTER_SIGNUP)




