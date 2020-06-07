from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time

class Popup():
    def test(self):
        # option = Options()
        # option.add_argument("--disable-infobars")
        # option.add_argument("--disable-extensions")
        # # Pass the argument 1 to allow and 2 to block
        # option.add_experimental_option("prefs", {
        #     "profile.default_content_setting_values.notifications": 2})
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.execute_script("window.location='https://letskodeit.teachable.com/p/practice';")
        driver.find_element_by_id("name").send_keys("test")
        driver.find_element_by_id("alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        driver.find_element_by_id("name").send_keys("test")
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        time.sleep(2)
pp=Popup()
pp.test()
