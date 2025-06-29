import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import LocatorsGeneral
from pages.base_page import BasePage
from urls import Urls

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    general = BasePage(driver)

    driver.maximize_window()
    driver.get(Urls.MAIN_PAGE)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LocatorsGeneral.BUTTON_COOKIE_ACCEPT))
    general.click_on_button_cookie_accept()

    yield driver

    driver.quit()