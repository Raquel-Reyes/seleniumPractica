import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver

        #Script de Danilo Bulux
        driver.get("https://trytestingthis.netlify.app/")
        driver.set_window_size(1532, 816)
        # Interactuar con los elementos de la página
        driver.find_element(By.ID, "fname").send_keys("Danilo")
        driver.find_element(By.ID, "lname").send_keys("Bulux")
        driver.find_element(By.ID, "male").click()
        dropdown = driver.find_element(By.ID, "option")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
        dropdown = driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
        driver.find_element(By.ID, "moption").click()
        driver.find_element(By.ID, "day").send_keys("07-06-2024")
        time.sleep(5)

        #Script de Iris González
        driver = webdriver.Chrome()
        driver.get("https://trytestingthis.netlify.app/")
        elem = driver.find_element(By.ID, "fnombre")
        elem.send_keys("Iris")
        elem = driver.find_element(By.ID, "lapellido")
        elem.send_keys("Gonzalez")

        #Script de Raquel Reyes
        driver.get('https://trytestingthis.netlify.app/')
        username_field = driver.find_element(By.ID, 'uname')
        username_field.send_keys('test')
        password_field = driver.find_element(By.ID, 'pwd')
        password_field.send_keys('test')
        #submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Login"]')
        #submit_button.click()
        time.sleep(5)

        #Script de Karen
        driver.get("https://trytestingthis.netlify.app/")
        elem = driver.find_element(By.ID, "fname")
        elem.send_keys("Karen")
        elem = driver.find_element(By.ID, "lname")
        elem.send_keys("Reyes")
        time.sleep(5)

        #Script de Isaac Tuiz
        # Selecciono mi color favorito
        driver.find_element(By.ID, "favcolor").send_keys("#008000")
        # Selecciono una cantidad
        driver.find_element(By.ID, "quantity").clear()
        driver.find_element(By.ID, "quantity").send_keys("10")
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()