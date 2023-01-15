from selenium import webdriver
from selenium.webdriver.common.by import By
import time


from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = (browser.find_element(By.ID, "num1"))
    num2 = (browser.find_element(By.ID, "num2"))
    x = int(num1.text)
    y = int(num2.text)
    sum =str(x + y)

    ans = Select(browser.find_element(By.ID, 'dropdown'))
    ans.select_by_value(sum)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    time.sleep(5)

finally:
    time.sleep(15)
    browser.quit()


