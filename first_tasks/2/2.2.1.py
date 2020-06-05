from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id('num1').text
    number2 = browser.find_element_by_id('num2').text
    summ = int(number1) + int(number2)
    summ_str = str(summ)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summ_str)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
