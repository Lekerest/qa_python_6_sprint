from selenium.webdriver.common.by import By


class LocatorsDropDownList:

    #Сколько это стоит? И как оплатить?
    FIRST_QUESTION = (By. ID, "accordion__heading-0")
    #Сутки — 400 рублей. Оплата курьеру — наличными или картой.
    FIRST_ANSWER = (By. ID, "accordion__panel-0")

    #Хочу сразу несколько самокатов! Так можно?
    SECOND_QUESTION = (By. ID, "accordion__heading-1")
    #Пока что у нас так: один заказ — один самокат.
    # Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.
    SECOND_ANSWER = (By. ID, "accordion__panel-1")

    #Как рассчитывается время аренды?
    THIRD_QUESTION = (By.ID, "accordion__heading-2")
    #Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня.
    # Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру.
    # Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.
    THIRD_ANSWER = (By.ID, "accordion__panel-2")

    #Можно ли заказать самокат прямо на сегодня?
    FOURTH_QUESTION = (By.ID, "accordion__heading-3")
    #Только начиная с завтрашнего дня. Но скоро станем расторопнее.
    FOURTH_ANSWER = (By.ID, "accordion__panel-3")

    #Можно ли продлить заказ или вернуть самокат раньше?
    FIFTH_QUESTION = (By.ID, "accordion__heading-4")
    #Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.
    FIFTH_ANSWER = (By.ID, "accordion__panel-4")

    #Вы привозите зарядку вместе с самокатом?
    SIXTH_QUESTION = (By.ID, "accordion__heading-5")
    #Самокат приезжает к вам с полной зарядкой.
    # Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.
    SIXTH_ANSWER = (By.ID, "accordion__panel-5")

    #Можно ли отменить заказ?
    SEVENTH_QUESTION = (By.ID, "accordion__heading-6")
    #Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.
    SEVENTH_ANSWER = (By.ID, "accordion__panel-6")

    #Я жизу за МКАДом, привезёте?
    EIGHTH_QUESTION = (By.ID, "accordion__heading-7")
    #Да, обязательно. Всем самокатов! И Москве, и Московской области.
    EIGHTH_ANSWER = (By.ID, "accordion__panel-7")
