from locators.locators_order_delivery import LocatorsOrderDelivery
from pages.page_order import PageOrder
from helpers import DataUser


class TestOrder:

    def test_order_through_top_button(self, driver):
        methods = PageOrder(driver)

        methods.click_on_top_button()

        methods.input_field_name(DataUser.FirstUserData['Name'])
        methods.input_field_surname(DataUser.FirstUserData['Surname'])
        methods.input_field_address(DataUser.FirstUserData['Address'])
        methods.select_station_metro(DataUser.FirstUserData['Metro'])
        methods.input_field_telephone_number(DataUser.FirstUserData['Telephone'])

        methods.click_button_next()

        methods.input_date_delivery(DataUser.FirstUserData['Date'])
        methods.select_colour(DataUser.FirstUserData['Colour'])

        methods.click_button_order_confirmation()

        element = driver.find_element(*LocatorsOrderDelivery.TEXT_ORDER_CREATED)
        assert element.is_displayed(), "Элемент TEXT_ORDER_CREATED не отображается на экране"
