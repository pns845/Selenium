from selenium import webdriver
class FromIdName():
    def test(self):
        baseURL="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.get(baseURL)
        element_by_id=driver.find_element_by_id("name")
        if element_by_id is not None:
            print("element found by id")
        else:
            print("element not found")
        element_by_name=driver.find_element_by_name("show-hide")
        if element_by_name is not None:
            print("element found by name")
        else:
            print("element not found")

c=FromIdName()
c.test()

