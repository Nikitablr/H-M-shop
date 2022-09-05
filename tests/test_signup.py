from pages.signup_page import SignupPage
from pages.base_page import BasePage

def test_signup_user(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = SignupPage(browser)
    page.open_signup_page()
    page.fill_fields_for_signup()