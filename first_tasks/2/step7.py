from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id('treasure')
    x_element = treasure.get_attribute('valuex')
    x = x_element
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    input1 = browser.find_element_by_id('robotCheckbox')
    input1.click()
    input2 = browser.find_element_by_id('robotsRule')
    input2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
