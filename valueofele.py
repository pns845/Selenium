from selenium import webdriver
import time
class GetAttributeValue():
    def test(self):
        baseURL="https://letskodeit.teachable.com/p/practice"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        element=driver.find_element_by_id("openwindow")
        print(element.get_attribute("id"))
        print(element.get_attribute("class"))
ga=GetAttributeValue()
ga.test()
