from selenium import webdriver
from os import path
from selenium.webdriver.common.by import By
import unittest
import time

class TestAbs(unittest.TestCase):

    def test_abs1(self):
        link = "http://suninjuly.github.io/registrationё1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        elements = browser.find_elements(By.CSS_SELECTOR, "div.first_block input")
        for element in elements:
            element.send_keys("Заполнено")
        assert len(elements) == 3

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        elements = browser.find_elements(By.CSS_SELECTOR, "div.first_block input")
        for element in elements:
            element.send_keys("Заполнено")
        assert len(elements) == 3

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

            # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()

