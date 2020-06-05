from selenium import webdriver
import time
class radioCheck():
    def test(self):
       # baseURL="https://www.expedia.com/?pwaLob=wizard-hotel-pwa-v2"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.implicitly_wait(5)
        radioElement=driver.find_element_by_id("bmwradio")
        radioElement.click()
        time.sleep(2)
        print('verifying that radio element is enabled or not' +str(radioElement.is_selected()))

        checkElement=driver.find_element_by_id("bmwcheck")
        checkElement.click()
        time.sleep(3)
        print('verifying that checkbox element is enabled or not'+str(checkElement.is_selected()))


ff=radioCheck()
ff.test()