import pytest
from selenium import webdriver
from data import Url


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Url.MAIN_PAGE_URL)
    yield driver
    driver.quit()
