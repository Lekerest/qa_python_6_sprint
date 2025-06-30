from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import LocatorsGeneral
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принять куки')
    def click_on_button_cookie_accept(self):
        return self.driver.find_element(*LocatorsGeneral.BUTTON_COOKIE_ACCEPT).click()

    @allure.step('Переход к элементу {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажатие на кнопку Яндекс')
    def click_on_button_yandex(self):
        return self.driver.find_element(*LocatorsGeneral.BUTTON_YANDEX).click()

    @allure.step('Нажатие на кнопку Самокат')
    def click_on_button_scooter(self):
        return self.driver.find_element(*LocatorsGeneral.BUTTON_SCOOTER).click()

    @allure.step('Получить ссылку')
    def get_url(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 5).until(EC.url_changes('about:blank'))
        return self.driver.current_url