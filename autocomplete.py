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
        time.sleep(3)
        wait=WebDriverWait(driver,15,poll_frequency=0.5,
                           ignored_exceptions=[ElementNotInteractableException,ElementNotSelectableException])
        x_path="//ul[@id='ui-id-1']//a[contains(text(),'Hyderabad, Pakistan - Hyderabad Airport (HDD)')]"
        element_from=wait.until(EC.element_to_be_clickable((By.XPATH,x_path)))
        element_from.click()
        time.sleep(3)
        print("from element clicked")
        to_element = driver.find_element_by_id("ToTag")
        to_element.send_keys("bang")
        element_to=wait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@id='ui-id-2']//a[contains(text(),'Bangkok, TH - Suvarnabhumi (BKK)')]")))
        element_to.click()
        time.sleep(3)
        destination_path="C:\\Users\\M524891\\OneDrive - myl\\desktop.sele.png"
        driver.save_screenshot(destination_path)
        print("screenshot saved at"+destination_path)
        print("to element clicked")
        driver.quit()

ac=AutoComplete()
ac.auto()

