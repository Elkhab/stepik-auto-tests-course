from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    a = browser.find_element_by_css_selector("#answer")
    a.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']").click()
    option2.click()
    option3 = browser.find_element_by_css_selector("label.form-check-label").click()
    option3.click()
    option4 = browser.find_element_by_css_selector("#robotsRule")
    option4.click()
    option5 = browser.find_element_by_css_selector("button.btn").click()
    option5.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

