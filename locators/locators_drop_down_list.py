from selenium.webdriver.common.by import By

class LocatorsDropDownList:
    #Сколько это стоит? И как оплатить?
    FIRST_QUESTION = (By. ID, "accordion__heading-0")

    #Хочу сразу несколько самокатов! Так можно?
    SECOND_QUESTION = (By. ID, "accordion__heading-1")

    #Как рассчитывается время аренды?
    THIRD_QUESTION = (By.ID, "accordion__heading-2")

    #Можно ли заказать самокат прямо на сегодня?
    FOURTH_QUESTION = (By.ID, "accordion__heading-3")

    #Можно ли продлить заказ или вернуть самокат раньше?
    FIFTH_QUESTION = (By.ID, "accordion__heading-4")

    #Вы привозите зарядку вместе с самокатом?
    SIXTH_QUESTION = (By.ID, "accordion__heading-5")

    #Можно ли отменить заказ?
    SEVENTH_QUESTION = (By.ID, "accordion__heading-6")

    #Я жизу за МКАДом, привезёте?
    EIGHTH_QUESTION = (By.ID, "accordion__heading-7")