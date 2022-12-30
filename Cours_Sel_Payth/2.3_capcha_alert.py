from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get(link)

  button_one = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
  button_one.click()
  # Согласиться, нажав на кнопку "Ок"
  confirm = browser.switch_to.alert
  confirm.accept()
  # взять значение в капче:
  # 2 Считать значение для переменной x.
  x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
  x = x_element.text
  # 3 Посчитать математическую функцию от x (код для этого приведён ниже).
  y = calc(x)
  # 4 Ввести ответ в текстовое поле.
  option1 = browser.find_element(By.CSS_SELECTOR, "#answer")
  option1.send_keys(y)
  # Нажать кнопку Submit (Отправить на проверку) Селектор скопирован из браузера
  button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
  button.click()
finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()


