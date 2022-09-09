import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    yield driver
    time.sleep(20)
    driver.quit()
