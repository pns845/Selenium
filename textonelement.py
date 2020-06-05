from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class GetText():
    def test(self):
        baseURL="https://letskodeit.teachable.com/p/practice"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        self.ele=driver.find_element(By.XPATH,"//div[@id='block-1069048']/div/div/div/div[3]/div[1]/fieldset/legend")
        ele_text=self.ele.text
        print(ele_text)

et=GetText()
et.test()

