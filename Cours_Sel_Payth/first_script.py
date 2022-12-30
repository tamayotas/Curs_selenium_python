
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, "submit_button")
    button.click()
    print('Кнопка нажата')

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    print('Браузер закрыт')


