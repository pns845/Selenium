from selenium import webdriver
import time

class JavaScript():
    def test(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.execute_script("window.location='https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(3)
        #driver.execute_script("window.scrollBy(0,1200);")
        time.sleep(2)
        #driver.execute_script("window.scrollBy(0,-1200);")
        time.sleep(2)
        #element = driver.execute_script("return document.getElementById('mousehover');")
        element =driver.find_element_by_id("mousehover")
        time.sleep(3)
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-300);")
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-1200);")
        location = element.location_once_scrolled_into_view
        print("location is"+str(location))
        time.sleep(3)
js=JavaScript()
js.test()