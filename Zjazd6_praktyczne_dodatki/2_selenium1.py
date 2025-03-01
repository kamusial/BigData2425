from selenium import webdriver
from selenium.webdriver import Keys
from time import sleep

okno1_chrome = webdriver.Chrome()
# okno2_firefox = webdriver.Firefox()
okno1_chrome.get('https://www.google.com/')
#okno2_firefox.get('https://allegro.pl')
sleep(3)
okno1_chrome.find_element('id','L2AGLb').click()
sleep(3)

search_field = okno1_chrome.find_element('name','q')
search_field.clear()
search_field.send_keys('Czy chat GPT opanuje świat?')
search_field.send_keys(Keys.ENTER)

sleep(3)


okno1_chrome.close()
#okno2_firefox.close()