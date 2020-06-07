# import os
# print(os.getcwd())
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class MouseHover():
    def test(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.execute_script("window.location='https://www.jqueryui.com/droppable/';")
        driver.implicitly_wait(3)
        driver.switch_to.frame(0)
        source_element = driver.find_element_by_id("draggable")
        target_element = driver.find_element_by_id("droppable")
        action_element = ActionChains(driver)
        #action_element.drag_and_drop(source_element,target_element).perform()
        action_element.click_and_hold(source_element).move_to_element(target_element).release().perform()
        time.sleep(2)
mh=MouseHover()
mh.test()