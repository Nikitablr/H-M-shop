import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    time.sleep(20)
    driver.quit()


