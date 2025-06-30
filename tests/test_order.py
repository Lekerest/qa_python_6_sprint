import allure
import pytest
from locators.locators_order_delivery import LocatorsOrderDelivery
from pages.page_order import PageOrder
from helpers import DataUser


class TestOrder:

    @pytest.mark.parametrize(
        "user_data, click_method_name",
        [
            (DataUser.FirstUserData, "click_on_top_button"),
            (DataUser.SecondUserData, "click_on_bot_button"),
        ]
    )
    @allure.title("Тест заказа: кнопка {click_method_name}, пользователь {user_data[Name]}")
    @allure.description("""
       Тест проверяет оформление заказа на сайте с использованием разных кнопок для вызова формы заказа:
       - верхняя кнопка "Заказать"
       - нижняя кнопка "Заказать"
       В тесте осуществляется заполнение формы заказчика, выбор параметров аренды и подтверждение заказа.
       Проверяется, что после оформления заказа появляется сообщение об успешном создании заказа.
       """)
    def test_order(self, driver, user_data, click_method_name):
        page = PageOrder(driver)

        click_method = getattr(page, click_method_name)
        click_method()

        page.input_field_name(user_data["Name"])
        page.input_field_surname(user_data["Surname"])
        page.input_field_address(user_data["Address"])
        page.select_station_metro(user_data["Metro"])
        page.input_field_telephone_number(user_data["Telephone"])

        page.click_button_next()
        page.input_date_delivery(user_data["Date"])
        page.click_body_page()
        page.select_rental_period(user_data["Rental Period"])
        page.select_colour(user_data["Colour"])

        page.click_button_order_created()
        page.click_button_order_confirmation()

        element = driver.find_element(*LocatorsOrderDelivery.TEXT_ORDER_CREATED)
        assert element.is_displayed(), "Элемент TEXT_ORDER_CREATED не отображается на экране"
