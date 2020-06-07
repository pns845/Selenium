from selenium import webdriver
import time

class iFrame():
    def test(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.execute_script("window.location='https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0,1000);")
        #driver.switch_to.frame("courses-iframe")
        time.sleep(2)
        #driver.switch_to.frame("iframe-name")
        driver.switch_to.frame(0)

        driver.find_element_by_id("search-courses").send_keys("python")
        time.sleep(3)
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,1000)")
        driver.find_element_by_id("name").send_keys("hello")
        time.sleep(3)

iFr=iFrame()
iFr.test()

