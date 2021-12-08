from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    a = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
      )
    button = browser.find_element_by_id("book")
    button.click()
    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    option4 = browser.find_element_by_css_selector("input#answer.form-control").send_keys(y)
    option5 = browser.find_element_by_css_selector("#solve").click()
    option5.click()
    
  
    
    

finally:
    print(a)
    # успеваем скопировать код за 30 секунд
    time.sleep(30)

    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

