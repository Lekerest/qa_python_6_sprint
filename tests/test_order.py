import pytest
from locators.locators_order_delivery import LocatorsOrderDelivery
from pages.page_order import PageOrder
from pages.base_page import BasePage
from helpers import DataUser


class TestOrder:

    @pytest.mark.parametrize(
        "user_data, button",
        [
            (DataUser.FirstUserData, "top"),
            (DataUser.SecondUserData, "bot"),
        ]
    )
    def test_order(self, driver, user_data, button):
        methods = PageOrder(driver)

        if button == "top":
            methods.click_on_top_button()
        elif button == "bot":
            BasePage(driver).scroll_to_element(LocatorsOrderDelivery.BUTTON_ORDER_BOTTOM_OF_THE_PAGE)
            methods.click_on_bot_button()

        methods.input_field_name(user_data['Name'])
        methods.input_field_surname(user_data['Surname'])
        methods.input_field_address(user_data['Address'])
        methods.select_station_metro(user_data['Metro'])
        methods.input_field_telephone_number(user_data['Telephone'])

        methods.click_button_next()

        methods.input_date_delivery(user_data['Date'])
        methods.click_body_page()
        methods.select_rental_period(user_data['Rental Period'])
        methods.select_colour(user_data['Colour'])

        methods.click_button_order_created()
        methods.click_button_order_confirmation()

        element = driver.find_element(*LocatorsOrderDelivery.TEXT_ORDER_CREATED)
        assert element.is_displayed(), "Элемент TEXT_ORDER_CREATED не отображается на экране"
