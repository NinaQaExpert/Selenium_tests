from unittest import TestCase
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

class TestForm(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home_url = 'http://127.0.0.1:5500/form.html'
        cls.driver = Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

    def test1_submit_form(self):
        self.driver.get(self.home_url)
        self.driver.save_screenshot('images/01_empty_page.png')
        self.driver.find_element(By.ID, 'user-id-box').send_keys('026589751')


        # Ввод ID
        self.driver.find_element(By.ID, 'user-id-box').send_keys('026589751')

        # Ввод имени
        self.driver.find_element(By.ID, 'user-name-box').send_keys('Daniel')
        self.driver.save_screenshot('images/02_fullname.png')

        # Установка даты рождения через JS
        birthdate_input = self.driver.find_element(By.ID, 'birthdate-box')
        birthdate_val = "1980-05-26"
        self.driver.execute_script('arguments[0].value = arguments[1];', birthdate_input, birthdate_val)


        self.driver.find_element(By.XPATH,'//*[@id="userForm"]/button').click()
        self.driver.save_screenshot('images/03_filled_form.png')
