from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class clickType():
    def test(self):
        baseURL="http://wa1dndbs001/ContractManagementDev/"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        userName=driver.find_element(By.ID,"inputmid")
        userName.send_keys("m222222")
        password=driver.find_element(By.ID,"inputPassword3")
        password.send_keys("1234")
        time.sleep(3)
        userName.clear()
        password.clear()
        userName.send_keys("m524891")
        time.sleep(3)
        password.send_keys("3423")
        signIn=driver.find_element(By.XPATH,"//button[@value='Sign In']")
        signIn.click()
ch=clickType()
ch.test()
#implicit wait ->