from locators.base_page_locators import LocatorsGeneral
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принять куки')
    def click_on_button_cookie_accept(self):
        return self.driver.find_element(*LocatorsGeneral.BUTTON_COOKIE_ACCEPT).click()

    @allure.step('Переход к вопросу {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

