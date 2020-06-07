from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class Slider():
    def test(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.execute_script("window.location='https://www.jqueryui.com/droppable/';")
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//div[@id='sidebar']//li/a[text()='Slider']").click()
        time.sleep(3)
        driver.switch_to.frame(0)
        slide_element = driver.find_element_by_xpath("//div[@id='slider']/span")
        action_obj = ActionChains(driver)
        action_obj.drag_and_drop_by_offset(slide_element,150,0).perform()
        time.sleep(2)
        print("slided successfully")

s=Slider()
s.test()

