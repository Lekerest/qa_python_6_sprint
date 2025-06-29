import allure
from pages.base_page import BasePage


class PageDropDownList(BasePage):

    @allure.step('Нажимаем на вопрос')
    def click_on_the_question(self, locator):
        return self.driver.find_element(*locator).click()

    @allure.step('Получаем текст FAQ')
    def get_text_faq(self, locator):
        return self.driver.find_element(*locator).text
