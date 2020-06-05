from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Calendar():
    def test(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        baseURL = "https://www.expedia.co.in/"
        driver.get(baseURL)
        driver.implicitly_wait(3)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").click()
        date_picker=driver.find_element(By.XPATH,"//div[@class='datepicker-cal-month'][position()=1]//button[@data-day='31']")
        date_picker.click()
        time.sleep(5)
        driver.quit()
        #//div[@class='datepicker-cal-month'][position()=1]//button[contains(text(),'31')]

c=Calendar()
c.test()