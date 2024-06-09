from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://trytestingthis.netlify.app/")

# Selecciono mi color favorito
driver.find_element(By.ID, "favcolor").send_keys("#008000")

# Selecciono una cantidad
driver.find_element(By.ID, "quantity").clear()
driver.find_element(By.ID, "quantity").send_keys("10")
time.sleep(10)