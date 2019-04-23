from selenium import webdriver
import time
import unittest
import spreadsheet
from loginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        profile_path = 'C:/FireFoxProfile'
        profile = webdriver.FirefoxProfile(profile_path)
        cls.driver = webdriver.Firefox(firefox_profile=profile_path)
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_login_valid(self):

        driver = self.driver
        driver.get('http://www.demo.guru99.com/V4/')

        path = "C://FireFoxProfile/login1.xlsx"

        rows = spreadsheet.getRowCount(path, 'Sheet1')

        login = LoginPage(driver)

        for r in range(2, rows + 1):
            username = spreadsheet.readData(path, "Sheet1", r, 1)
            password = spreadsheet.readData(path, "Sheet1", r, 2)
            login.enter_username(username)
            login.enter_password(password)
            login.click_login()

            if driver.title == "Guru99 Bank Manager HomePage":
                print("test is passed")
                spreadsheet.writeData(path, "Sheet1", r, 3, "test passed")
                driver.get('http://www.demo.guru99.com/V4/')
            else:
                print("test failed")
                spreadsheet.writeData(path, "Sheet1", r, 3, "test failed")
            # return to homepage and insert password/username for next row in spreadsheet this line does not work
                WebDriverWait(driver, 300).until(EC.alert_is_present).accept
                time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
