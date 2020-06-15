from selenium import webdriver
import time
from page_exam_package.homepage.login_page import LoginTest
import unittest
import pytest

class TestLogin(unittest.TestCase):
    baseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get(baseURL)
    driver.implicitly_wait(3)
    time.sleep(3)
    lp = LoginTest(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get(self.baseURL)
        self.lp.test_Login("test@email.com","abcabc")
        time.sleep(3)
        result = self.lp.verify_Loginsuccessful()
        assert result == True
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.test_Login(password="abcabc")
        time.sleep(3)
        result = self.lp.verify_Login_Failed()
        assert result == True
    driver.quit()




