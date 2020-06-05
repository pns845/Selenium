from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
class dropDown():
    def test(self):
       # baseURL="https://www.expedia.com/?pwaLob=wizard-hotel-pwa-v2"
       driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
       driver.maximize_window()
       driver.get("https://letskodeit.teachable.com/p/practice")
       driver.implicitly_wait(3)
       dropelement =driver.find_element(By.ID,"carselect")
       sel = Select(dropelement)
       sel.select_by_value("benz")
       time.sleep(3)
       sel.select_by_index(2)
       time.sleep(3)
       sel.select_by_visible_text("BMW")
       time.sleep(3)
       driver.quit()
dd=dropDown()
dd.test()

