from selenium import webdriver
import time
class radioCheck():
    def test(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.implicitly_wait(5)
        elementsList=driver.find_elements_by_xpath("//input[contains(@name,'cars') and contains(@type,'checkbox')]")
        length=len(elementsList)
        for element in elementsList:
            cselected=element.is_selected()
            time.sleep(2)
            if not cselected:
                element.click()
                time.sleep(2)

r=radioCheck()
r.test()

