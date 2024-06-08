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


        #Script de Iris González
                

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


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()