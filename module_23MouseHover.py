from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class MouseHover():
    def test(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.execute_script("window.location='https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0,600);")
        mouse_element = driver.find_element_by_id("mousehover")
        actionobj = ActionChains(driver)
        actionobj.move_to_element(mouse_element).perform()
        time.sleep(2)
        toplink = driver.find_element_by_xpath("//div[@class='mouse-hover-content']/a[text()='Top']")
        actionobj.move_to_element(toplink).click().perform()
        time.sleep(2)
mh = MouseHover()
mh.test()

