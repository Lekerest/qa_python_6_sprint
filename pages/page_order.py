import allure
from locators.locators_order_delivery import LocatorsOrderDelivery
from pages.base_page import BasePage


class PageOrder(BasePage):

    @allure.step('Переход в форму заказа по верхней кнопке')
    def click_on_top_button(self):
        return self.driver.find_element(*LocatorsOrderDelivery.BUTTON_ORDER_FROM_ABOVE).click()

    @allure.step('Переход в форму заказа по нижней кнопке')
    def click_on_bot_button(self):
        return self.driver.find_element(*LocatorsOrderDelivery.BUTTON_ORDER_BOTTOM_OF_THE_PAGE).click()

    @allure.step('Ввод в поле Имя')
    def input_field_name(self, field_name):
        return self.driver.find_element(*LocatorsOrderDelivery.FIELD_NAME).send_keys(field_name)

    @allure.step('Ввод в поле Фамилия')
    def input_field_surname(self, field_surname):
        return self.driver.find_element(*LocatorsOrderDelivery.FIELD_SURNAME).send_keys(field_surname)

    @allure.step('Ввод в поле Адрес')
    def input_field_address(self, field_address):
        return self.driver.find_element(*LocatorsOrderDelivery.FIELD_ADDRESS).send_keys(field_address)

    @allure.step('Ввод в поле Телефон')
    def input_field_telephone_number(self, field_telephone):
        return self.driver.find_element(*LocatorsOrderDelivery.FIELD_TELEPHONE_NUMBER).send_keys(field_telephone)

    @allure.step('Выбор станции метро')
    def select_station_metro(self, station_metro):
        self.driver.find_element(*LocatorsOrderDelivery.FIELD_STATION_METRO).click()
        return self.driver.find_element(*station_metro).click()

    @allure.step('Выбор даты доставки')
    def input_date_delivery(self, date_delivery):
        self.driver.find_element(*LocatorsOrderDelivery.FIELD_DATE_DELIVERY).click()
        return self.driver.find_element(*LocatorsOrderDelivery.FIELD_DATE_DELIVERY).send_keys(date_delivery)

    @allure.step('Выбор срока аренды')
    def select_rental_period(self, rental_period):
        self.driver.find_element(*LocatorsOrderDelivery.FIELD_RENTAL_PERIOD).click()
        return self.driver.find_element(*rental_period).click()

    @allure.step('Выбор цвета')
    def select_colour(self, colour):
        return self.driver.find_element(*colour).click()

    @allure.step('Ввод комментария')
    def input_comment_for_runner(self, comment):
        return self.driver.find_element(*LocatorsOrderDelivery.FIELD_COMMENT_FOR_COURIER).send_keys(comment)

    @allure.step('Нажимаем кнопку заказать')
    def click_button_order_created(self):
        return self.driver.find_element(*LocatorsOrderDelivery.BUTTON_ORDER_CREATED).click()

    @allure.step('Нажимаем кнопку далее')
    def click_button_next(self):
        return self.driver.find_element(*LocatorsOrderDelivery.BUTTON_NEXT).click()

    @allure.step('Подтверждаем заказ')
    def click_button_order_confirmation(self):
        return self.driver.find_element(*LocatorsOrderDelivery.BUTTON_ORDER_CONFIRMATION).click()

    @allure.step('Клик по странице')
    def click_body_page(self):
        return self.driver.find_element(*LocatorsOrderDelivery.BODY_PAGE).click()
