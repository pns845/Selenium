from selenium import webdriver
import time
from base_exam_package.selenium_driver import SeleniumDriver
import utilities_exam_package.customLogger as cl
import logging

class LoginTest(SeleniumDriver):
    log = cl.custom_Logger()
    def __init__(self,driver):
        super().__init__()
        self.driver = driver
        # Locators
        self.login_link = "Login"
        self.user_field = "user_email"
        self.password = "user_password"
        self.login_button = "commit"

    def getLoginlink(self):
        self.elementClick(self.login_link,locatorType="link")
    def getUserName(self,email):
        self.sendKeys(email ,self.user_field)
    def getPassword(self,password):
        self.sendKeys(password,self.password)
    def getLoginbutton(self):
        self.elementClick(self.login_button,locatorType="name")

    def test_Login(self,email="",password=""):
        self.getLoginlink()
        self.clearFields()
        self.getUserName(email)
        time.sleep(3)
        self.getPassword(password)
        time.sleep(3)
        self.getLoginbutton()
    def verify_Loginsuccessful(self):
        result = self.isElementPresent("search-courses" ,"id")
        return result
    def verify_Login_Failed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]","xpath")
        return result
    def clearFields(self):
        emailField = self.getElement(self.user_field,"id")
        emailField.clear()
        passwordField = self.getElement(self.password,"id")
        passwordField.clear()







