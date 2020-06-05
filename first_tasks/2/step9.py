from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('mur')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('mur')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('mur@mur')

    file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname('step9.py'))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'footer.py')           # добавляем к этому пути имя файла
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
