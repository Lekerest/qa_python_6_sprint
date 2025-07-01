from selenium.webdriver.common.by import By

class LocatorsGeneral:
    #Кнопка принять куки
    BUTTON_COOKIE_ACCEPT = (By.ID, 'rcc-confirm-button')

    #Кнопка яндекс
    BUTTON_YANDEX = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')

    #Кнопка самокат
    BUTTON_SCOOTER = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')
