from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.signin_locators import SigninLocators


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'https://www2.hm.com/en_us/index.html'

    def go_to_site(self):
        self.browser.get(self.base_url)
        cookies = self.browser.find_element(*SigninLocators.ACCEPT_ALL_COOKIES_BUTTON)
        cookies.click()

    def scroll_to_element(self, *how):
        element = self.browser.find_element(*how)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    def click(self, *locator):
        element = self.browser.find_element(*locator)
        element.click()

    def fill(self, value, locator, wait_time=60):
        element = self.browser.find_element(locator, wait_time)
        if value:
            element.send_keys(value)


    def is_presented(self, *how):
        element = self.browser.find_element(*how)
        return element is not None

    def hover_to_element(self, *how):
        element_to_hover_over = self.browser.find_element(*how)
        hover = ActionChains(self.browser)
        hover.move_to_element(element_to_hover_over)
        hover.perform()

    def wait_to_be_clickable(self, locator):
        try:
            element = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            return False

        return True

    def switch_to_new_window(self, num_win):
        self.browser.switch_to.window(self.browser.window_handles[int(num_win)])





