from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import LocatorsGeneral
import allure

class PageDropDownList:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход к вопросу {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_the_question(self, locator):
        return self.driver.find_element(*locator).click()

    def get_text_question(self, locator):
        return self.driver.find_element(*locator).text

