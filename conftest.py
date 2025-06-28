import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from urls import Urls

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.MAIN_PAGE)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable())
    yield driver
    driver.quit()