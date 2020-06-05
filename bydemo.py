from selenium import webdriver
from selenium.webdriver.common.by import By
class ByDemo():
    def test(self):
        baseURL="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.get(baseURL)
        element_id=driver.find_element(By.ID,"name")
        if element_id is not None:
            print("element found by id")
        else:
            print("element not found")
        element_xpath=driver.find_element(By.XPATH,"//input[@id='displayed-text']")
        if element_xpath is not None:
            print("element found by xpath")
        else:
            print("element not found")
        element_linktext=driver.find_element(By.LINK_TEXT,"Login")
        if element_linktext is not None:
            print("element found by link text")
        else:
            print("element not found")

cc=ByDemo()
cc.test()


