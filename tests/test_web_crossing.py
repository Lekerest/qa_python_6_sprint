from pages.base_page import BasePage
from urls import Urls
import pytest

class TestWebCrossing:

    def test_web_crossing_on_dzen(self, driver):
        web_crossing = BasePage(driver)
        web_crossing.click_on_button_yandex()

        assert 'dzen.ru' in web_crossing.get_url()

    @pytest.mark.parametrize('driver', [2], indirect=True)
    def test_web_crossing_on_scooter(self, driver):
        web_crossing = BasePage(driver)
        web_crossing.click_on_button_scooter()

        assert web_crossing.get_url() == Urls.MAIN_PAGE
