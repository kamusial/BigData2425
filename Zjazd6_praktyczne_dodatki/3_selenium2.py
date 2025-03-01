from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import datetime

def make_screenshot(window):
    teraz = datetime.datetime.now()
    filename = teraz.strftime('screens\\screenshot_%H_%M_%S.png')
    window.get_screenshot_as_file(filename)

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

try:
    username_field = driver.find_element(By.ID, 'user-nameQQQQ')
    password_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
except:
    print('nie znaleziono')
    make_screenshot(driver)
    driver.quit()
    raise

username_field.clear()
username_field.send_keys('standard_user')
password_field.clear()
password_field.send_keys('secret_sauce')
login_button.click()

sleep(2)