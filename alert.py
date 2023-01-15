from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

    mini_but = browser.switch_to.alert
    mini_but.accept()

    input_value = browser.find_element(By.ID, 'input_value')
    x = input_value.text
    ans = calc(x)

    input1= browser.find_element(By.ID, 'answer')
    input1.send_keys(ans)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

    time.sleep(5)

finally:
    time.sleep(5)
    browser.quit()

    