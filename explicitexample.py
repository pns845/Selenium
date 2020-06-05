from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expec
from selenium.common.exceptions import *
import time

class ExplicitWaits():
    def test(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        baseURL="https://www.expedia.co.in/"
        driver.get(baseURL)
        driver.implicitly_wait(3)
        driver.find_element(By.ID,"tab-flight-tab-hp").click()
        driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("01/06/2020")
        time.sleep(2)
        return_Date=driver.find_element(By.ID,"flight-returning-hp-flight")
        return_Date.click()
        time.sleep(3)
        # return_Date.clear()
        # time.sleep(2)
        # return_Date.send_keys("06/16/2020")
        driver.find_element(By.XPATH,"//form[@id='gcw-flights-form-hp-flight']/div[9]//button").click()
        #driver.find_element(By.ID,"stopFilter_stops-0").click()
        wait=WebDriverWait(driver,10,poll_frequency=2,
                           ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
        element=wait.until(Expec.element_to_be_clickable((By.ID,"stopFilter_stops-0")))
        element.click()
        time.sleep(5)
        driver.quit()

ex=ExplicitWaits()
ex.test()


