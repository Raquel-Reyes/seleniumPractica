from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://trytestingthis.netlify.app/')
username_field = driver.find_element(By.ID, 'uname')
username_field.send_keys('test')
password_field = driver.find_element(By.ID, 'pwd')
password_field.send_keys('test')
submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Login"]')
submit_button.click()
time.sleep(10)