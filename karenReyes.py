from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://trytestingthis.netlify.app/")
elem = driver.find_element(By.ID, "fname")
elem.send_keys("Karen")
elem = driver.find_element(By.ID, "lname")
elem.send_keys("Reyes")

time.sleep(15)