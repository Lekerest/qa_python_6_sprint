from selenium.webdriver.common.by import By


class LocatorsOrderDelivery:

    #Кнопка заказать наверху страницы
    BUTTON_ORDER_FROM_ABOVE = (By.CSS_SELECTOR, '.Button_Button__ra12g')

    #Кнопка заказать внизу страницы
    BUTTON_ORDER_BOTTOM_OF_THE_PAGE = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_UltraBig__UU3Lp')

    #Поле Имя
    FIELD_NAME = (By.CSS_SELECTOR, '.Input_Input__1iN_Z.Input_Error__1Tx5d.Input_Responsible__1jDKN')

    #Поле Фамилия
    FIELD_SURNAME = (By.XPATH, ".//*[@placeholder='* Фамилия']")

    #Поле адрес
    FIELD_ADDRESS = (By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']")

    #Поле станция метро
    FIELD_STATION_METRO = (By.XPATH, ".//*[@placeholder='* Станция метро']")

    #Станция бульвар рокоссовского
    BUTTON_STATION_BULVAR_ROCOSOVSKOGO = (By.XPATH, ".//button[(@class='Order_SelectOption__82bhS select-search__option is-selected')]")

    #Станция Черкизовская
    BUTTON_STATION_CHERKIZOVKAYA = (By.XPATH, ".//button[(@class='Order_SelectOption__82bhS select-search__option') and (@value='2')]")

    #Поле телефон
    FIELD_TELEPHONE_NUMBER = (By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']")

    #Дата доставки
    FIELD_DATE_DELIVERY = (By.XPATH, ".//*[@placeholder='* Когда привезти самокат']")

    #Поле срок аренды
    FIELD_RENTAL_PERIOD = (By.CSS_SELECTOR, '.Dropdown-placeholder')

    #Кнопка сутки
    BUTTON_ONE_DAY = (By.XPATH, ".//div[(@class='Dropdown-option') and (text()='сутки')]")

    #Кнопка двое суток
    BUTTON_TWO_DAY = (By.XPATH, ".//div[(@class='Dropdown-option') and (text()='двое суток')]")

    #Чекбокс цвет самоката - черный
    CHECKBOX_COLOR_SCOOTER_BLACK = (By.ID, "black")

    #Чекбокс цвет самоката - серый
    CHECKBOX_COLOR_SCOOTER_GREY = (By.ID, "grey")

    #Поле комментарий
    FIELD_COMMENT_FOR_COURIER = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")

    #Кнопка далее
    BUTTON_NEXT = (By.CSS_SELECTOR, "Button_Button__ra12g Button_Middle__1CSJM")

    #Кнопка подтверждение заказа
    BUTTON_ORDER_CONFIRMATION = (By.XPATH, ".//button[(@class='Button_Button__ra12g Button_Middle__1CSJM') and (text()='Да')]")

    #Текст Заказ оформлен
    TEXT_ORDER_CREATED = (By.XPATH, ".//button[(@class='Order_ModalHeader__3FDaJ') and (text()='Заказ оформлен')]")
