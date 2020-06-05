#to find all the tags are present or all buttons are present
#finding multiple elements
from selenium import webdriver
from selenium.webdriver.common.by import By
class FindList():
    def test(self):
        baseURL="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.get(baseURL)
        elements_id=driver.find_elements_by_id("name")
        list1=len(elements_id)
        print("the number of webelements with same id are"+str(list1))
        elements_tag=driver.find_elements(By.TAG_NAME,"a")
        list2=len(elements_tag)
        print("the number of webelements with same tag are" +str(list2))
        # for i in range(list2):
        #     print(i.__getattribute__())
c=FindList()
c.test()