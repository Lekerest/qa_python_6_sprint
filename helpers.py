from locators.locators_order_delivery import LocatorsOrderDelivery


class FAQDropDownList:
    FIRST_QUESTION = 'Сколько это стоит? И как оплатить?'
    SECOND_QUESTION = 'Хочу сразу несколько самокатов! Так можно?'
    THIRD_QUESTION = 'Как рассчитывается время аренды?'
    FOURTH_QUESTION = 'Можно ли заказать самокат прямо на сегодня?'
    FIFTH_QUESTION = 'Можно ли продлить заказ или вернуть самокат раньше?'
    SIXTH_QUESTION = 'Вы привозите зарядку вместе с самокатом?'
    SEVENTH_QUESTION = 'Можно ли отменить заказ?'
    EIGHTH_QUESTION = 'Я жизу за МКАДом, привезёте?'

    FIRST_ANSWER = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    SECOND_ANSWER = ('Пока что у нас так: один заказ — один самокат. '
                     'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')
    THIRD_ANSWER = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                    'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                    'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    FOURTH_ANSWER = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    FIFTH_ANSWER = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    SIXTH_ANSWER = ('Самокат приезжает к вам с полной зарядкой. '
                    'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')
    SEVENTH_ANSWER = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    EIGHTH_ANSWER = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


    FaqList = {
    FIRST_QUESTION : FIRST_ANSWER,
    SECOND_QUESTION : SECOND_ANSWER,
    THIRD_QUESTION : THIRD_ANSWER,
    FOURTH_QUESTION : FOURTH_ANSWER ,
    FIFTH_QUESTION : FIFTH_ANSWER,
    SIXTH_QUESTION : SIXTH_ANSWER,
    SEVENTH_QUESTION : SEVENTH_ANSWER,
    EIGHTH_QUESTION : EIGHTH_ANSWER}

class DataUser:

    Metro = [LocatorsOrderDelivery.BUTTON_STATION_BULVAR_ROCOSOVSKOGO, LocatorsOrderDelivery.BUTTON_STATION_CHERKIZOVKAYA]
    Colour = {
        'Grey' : LocatorsOrderDelivery.CHECKBOX_COLOR_SCOOTER_GREY,
        'Black' : LocatorsOrderDelivery.CHECKBOX_COLOR_SCOOTER_BLACK
    }
    FirstUserData = {
        'Name' : 'Иван',
        'Surname': 'Иванов',
        'Address': 'Иванова 12',
        'Metro': Metro[0],
        'Telephone': 112233445566,
        'Date': '1.1.35',
        'Colour': Colour['Grey'],}
