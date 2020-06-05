import time
# print(time.time())
# print(time.time()*1000)
# print(round(time.time()*1000))
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class AutoComplete():

    def auto(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.cleartrip.com"
        driver.get(baseURL)
        driver.implicitly_wait(5)
        origin_element=driver.find_element_by_id('FromTag')
        origin_element.send_keys("hyd")
        self.Screenshot(driver)
        time.sleep(3)
        wait = WebDriverWait(driver,15,poll_frequency=0.5,
                           ignored_exceptions=[ElementNotInteractableException,ElementNotSelectableException])
        x_path="//ul[@id='ui-id-1']//a[contains(text(),'Hyderabad, Pakistan - Hyderabad Airport (HDD)')]"
        element_from = wait.until(EC.element_to_be_clickable((By.XPATH,x_path)))
        element_from.click()
        time.sleep(3)
        print("from element clicked")
        to_element = driver.find_element_by_id("ToTag")
        to_element.send_keys("bang")
        self.Screenshot(driver)
        element_to=wait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@id='ui-id-2']//a[contains(text(),'Bangkok, TH - Suvarnabhumi (BKK)')]")))
        element_to.click()
        time.sleep(3)
        self.Screenshot(driver)
        driver.quit()

    def Screenshot(self,driver):
        destination_path="C:\\Users\\M524891\\OneDrive - myl\\desktop\\"
        file_name=str(round(time.time()*1000))+".png"
        destination_file=destination_path+file_name
        driver.save_screenshot(destination_file)
        print("screenshot saved at"+destination_file)
        print("to element clicked")


ac=AutoComplete()
ac.auto()


