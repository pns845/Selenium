from selenium import webdriver
import time

class JavaScript():
    def test(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        height_1 = driver.execute_script("return window.innerHeight;")
        print("height of the window before maximize is " + str(height_1))
        width_1 = driver.execute_script("return window.innerWidth")
        print("width of window before maximize is " + str(width_1))
        driver.maximize_window()
        driver.execute_script("window.location='https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(3)
        height = driver.execute_script("return window.innerHeight;")
        print("height of the window after maximize is "+str(height))
        width = driver.execute_script("return window.innerWidth")
        print("width of window after maximize is "+str(width))
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")
        time.sleep(3)
js=JavaScript()
js.test()
