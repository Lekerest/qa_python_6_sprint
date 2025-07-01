from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from locators.base_page_locators import LocatorsGeneral
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента {locator}')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу {locator}')
    def click_element(self, locator):
        return self.find_element(locator).click()

    @allure.step('Ввод значения в элемент {locator}')
    def send_keys_to_element(self, locator, value):
        return self.find_element(locator).send_keys(value)

    @allure.step('Ожидание изменения URL с {old_url}')
    def wait_for_url_change(self, old_url, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))

    @allure.step('Переключение на последнюю вкладку')
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Скролл к элементу {locator}')
    def scroll_to(self, locator):
        element = self.find_element(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Принять куки')
    def click_on_button_cookie_accept(self):
        return self.click_element(LocatorsGeneral.BUTTON_COOKIE_ACCEPT)

    @allure.step('Переход к элементу {locator}')
    def scroll_to_element(self, locator):
        return self.scroll_to(locator)

    @allure.step('Нажатие на кнопку Яндекс')
    def click_on_button_yandex(self):
        return self.click_element(LocatorsGeneral.BUTTON_YANDEX)

    @allure.step('Нажатие на кнопку Самокат')
    def click_on_button_scooter(self):
        return self.click_element(LocatorsGeneral.BUTTON_SCOOTER)

    @allure.step('Получить ссылку')
    def get_url(self):
        self.switch_to_last_window()
        self.wait_for_url_change('about:blank')
        return self.driver.current_url

    @allure.step('Ожидание отображения элемента {locator}')
    def wait_for_element_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Проверка, отображается ли элемент {locator}')
    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except NoSuchElementException:
            return False