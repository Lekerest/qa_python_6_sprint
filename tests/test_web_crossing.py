import allure
import pytest
from pages.base_page import BasePage
from urls import Urls


class TestWebCrossing:

    @allure.title("Переход на сайт Яндекс.Дзен")
    @allure.description("Проверка, что при клике на кнопку Яндекс происходит переход на dzen.ru")
    def test_web_crossing_on_dzen(self, driver):
        web_crossing = BasePage(driver)
        web_crossing.click_on_button_yandex()
        assert "dzen.ru" in web_crossing.get_url(), "Переход на Dzen не выполнен"

    @allure.title("Переход на главную страницу по кнопке Самокат")
    @allure.description("Проверка, что при клике на кнопку Самокат происходит переход на главную страницу")
    @pytest.mark.parametrize("driver", [2], indirect=True)
    def test_web_crossing_on_scooter(self, driver):
        web_crossing = BasePage(driver)
        web_crossing.click_on_button_scooter()
        assert web_crossing.get_url() == Urls.MAIN_PAGE, "URL после перехода не совпадает с ожидаемым"
