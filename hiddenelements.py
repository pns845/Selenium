from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class dropDown():
    def test(self):
       # baseURL="https://www.expedia.com/?pwaLob=wizard-hotel-pwa-v2"
       driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
       driver.maximize_window()
       driver.get("https://letskodeit.teachable.com/p/practice")
       driver.implicitly_wait(3)
       checkb=driver.find_element(By.ID,"displayed-text")
       element_hide=driver.find_element(By.ID,"hide-textbox")
       element_hide.click()
       time.sleep(3)
       print("the textbox is displayed or not on clicking hide-"+str(checkb.is_displayed()))
       element_show=driver.find_element(By.ID,"show-textbox")
       element_show.click()
       time.sleep(3)
       print("the textbox is displayed or not on clicking show -"+str(checkb.is_displayed()))
dd=dropDown()
dd.test()