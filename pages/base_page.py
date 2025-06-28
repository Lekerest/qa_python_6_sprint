from locators.base_page_locators import LocatorsGeneral
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принять куки')
    def click_on_button_cookie_accept(self):
        return self.driver.find_element(*LocatorsGeneral.BUTTON_COOKIE_ACCEPT).click()
