from selenium import webdriver
class Findbyxpath():
    def test(self):
        baseURL="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.get(baseURL)
        element_by_xpath=driver.find_element_by_xpath("//input[@id='name']")
        if element_by_xpath is not None:
            print("element found by xpath")
        else:
            print("element not found")
        element_by_css=driver.find_element_by_css_selector("#displayed-text")
        if element_by_css is not None:
            print("element found by css")
        else:
            print("element not found")

c=Findbyxpath()
c.test()