from urllib.parse import urljoin

class Urls:
    MAIN_PAGE = "https://qa-scooter.praktikum-services.ru/"

    ORDER_PAGE = urljoin(MAIN_PAGE, "/order")

    DZEN_PAGE = urljoin(MAIN_PAGE, "https://dzen.ru")