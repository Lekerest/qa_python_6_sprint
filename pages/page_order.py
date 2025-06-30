import allure
from locators.locators_order_delivery import LocatorsOrderDelivery
from pages.base_page import BasePage


class PageOrder(BasePage):

    @allure.step('Переход в форму заказа по верхней кнопке')
    def click_on_top_button(self):
        return self.click_element(LocatorsOrderDelivery.BUTTON_ORDER_FROM_ABOVE)

    @allure.step('Переход в форму заказа по нижней кнопке')
    def click_on_bot_button(self):
        return self.click_element(LocatorsOrderDelivery.BUTTON_ORDER_BOTTOM_OF_THE_PAGE)

    @allure.step('Ввод в поле Имя')
    def input_field_name(self, field_name):
        return self.send_keys_to_element(LocatorsOrderDelivery.FIELD_NAME, field_name)

    @allure.step('Ввод в поле Фамилия')
    def input_field_surname(self, field_surname):
        return self.send_keys_to_element(LocatorsOrderDelivery.FIELD_SURNAME, field_surname)

    @allure.step('Ввод в поле Адрес')
    def input_field_address(self, field_address):
        return self.send_keys_to_element(LocatorsOrderDelivery.FIELD_ADDRESS, field_address)

    @allure.step('Ввод в поле Телефон')
    def input_field_telephone_number(self, field_telephone):
        return self.send_keys_to_element(LocatorsOrderDelivery.FIELD_TELEPHONE_NUMBER, field_telephone)

    @allure.step('Выбор станции метро')
    def select_station_metro(self, station_metro):
        self.click_element(LocatorsOrderDelivery.FIELD_STATION_METRO)
        return self.click_element(station_metro)

    @allure.step('Выбор даты доставки')
    def input_date_delivery(self, date_delivery):
        self.click_element(LocatorsOrderDelivery.FIELD_DATE_DELIVERY)
        return self.send_keys_to_element(LocatorsOrderDelivery.FIELD_DATE_DELIVERY, date_delivery)

    @allure.step('Выбор срока аренды')
    def select_rental_period(self, rental_period):
        self.click_element(LocatorsOrderDelivery.FIELD_RENTAL_PERIOD)
        return self.click_element(rental_period)

    @allure.step('Выбор цвета')
    def select_colour(self, colour):
        return self.click_element(colour)

    @allure.step('Ввод комментария')
    def input_comment_for_runner(self, comment):
        return self.send_keys_to_element(LocatorsOrderDelivery.FIELD_COMMENT_FOR_COURIER, comment)

    @allure.step('Нажимаем кнопку заказать')
    def click_button_order_created(self):
        return self.click_element(LocatorsOrderDelivery.BUTTON_ORDER_CREATED)

    @allure.step('Нажимаем кнопку далее')
    def click_button_next(self):
        return self.click_element(LocatorsOrderDelivery.BUTTON_NEXT)

    @allure.step('Подтверждаем заказ')
    def click_button_order_confirmation(self):
        return self.click_element(LocatorsOrderDelivery.BUTTON_ORDER_CONFIRMATION)

    @allure.step('Клик по странице')
    def click_body_page(self):
        return self.click_element(LocatorsOrderDelivery.BODY_PAGE)

    @allure.step('Проверяем отображение текста об успешном заказе')
    def is_order_created_text_displayed(self):
        return self.is_element_displayed(LocatorsOrderDelivery.TEXT_ORDER_CREATED)

    @allure.step('Ожидание появления текста об успешном заказе')
    def wait_for_order_created_text(self):
        return self.wait_for_element_visible(LocatorsOrderDelivery.TEXT_ORDER_CREATED)
