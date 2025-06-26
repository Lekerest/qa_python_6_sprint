from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPageMesto:
    driver = webdriver.Firefox()  # вместо Chrome()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.maximize_window()
    driver.quit()