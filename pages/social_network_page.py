from pages.base_page import BasePage
from locators.locators_main_page import *

class SocialNetworkPage(BasePage):

    def open_facebook_page(self):
        self.browser.find_element(*SocialNetworkLocators.FACEBOOK_PAGE_BUTTON)
        self.scroll_to_element(*SocialNetworkLocators.FACEBOOK_PAGE_BUTTON)
        self.click(*SocialNetworkLocators.FACEBOOK_PAGE_BUTTON)
        assert 'Facebook' and 'H&M' in self.browser.title

    def open_twitter_page(self):
        self.browser.find_element(*SocialNetworkLocators.TWITTER_PAGE_BUTTON)
        self.scroll_to_element(*SocialNetworkLocators.TWITTER_PAGE_BUTTON)
        self.click(*SocialNetworkLocators.TWITTER_PAGE_BUTTON)
        assert 'Twitter' and 'H&M' in self.browser.title

    def open_instagram_page(self):
        self.browser.find_element(*SocialNetworkLocators.INSTAGRAM_PAGE_BUTTON)
        self.scroll_to_element(*SocialNetworkLocators.INSTAGRAM_PAGE_BUTTON)
        self.click(*SocialNetworkLocators.INSTAGRAM_PAGE_BUTTON)
        assert 'Instagram' and 'H&M' in self.browser.title

    def open_youtube_page(self):
        self.browser.find_element(*SocialNetworkLocators.YOUTUBE_PAGE_BUTTON)
        self.scroll_to_element(*SocialNetworkLocators.YOUTUBE_PAGE_BUTTON)
        self.click(*SocialNetworkLocators.YOUTUBE_PAGE_BUTTON)
        assert 'YouTube' and 'H&M' in self.browser.title

    def open_pinterest_page(self):
        self.browser.find_element(*SocialNetworkLocators.PINTEREST_PAGE_BUTTON)
        self.scroll_to_element(*SocialNetworkLocators.PINTEREST_PAGE_BUTTON)
        self.click(*SocialNetworkLocators.PINTEREST_PAGE_BUTTON)
        assert 'Pinterest' and 'H&M' in self.browser.title





