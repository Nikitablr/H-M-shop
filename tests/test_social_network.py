from pages.base_page import BasePage
from pages.social_network_page import SocialNetworkPage


def test_facebook_page_link(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = SocialNetworkPage(browser)
    page.open_facebook_page()

def test_twitter_page_link(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = SocialNetworkPage(browser)
    page.open_twitter_page()

def test_instagram_page_link(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = SocialNetworkPage(browser)
    page.open_instagram_page()

def test_yotube_page_link(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = SocialNetworkPage(browser)
    page.open_youtube_page()

def test_pinterest_page_link(browser):
    page = BasePage(browser)
    page.go_to_site()
    page = SocialNetworkPage(browser)
    page.open_youtube_page()
