from selenium import webdriver
import time

class Switch():
    def test(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.execute_script("window.location='https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(3)
        parent_handle=driver.current_window_handle
        print("Parent Handle is "+parent_handle)
        driver.find_element_by_id("openwindow").click()
        time.sleep(2)
        sub_Handles = driver.window_handles
        for handle in sub_Handles:
            print(handle)
            print(type(handle))
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print("Currently in child handle")
                driver.find_element_by_id("search-courses").send_keys("Python")
                time.sleep(2)
                break
        driver.switch_to.window(parent_handle)
        driver.find_element_by_id("name").send_keys("testing done")
        time.sleep(3)
        driver.quit()

s=Switch()
s.test()
