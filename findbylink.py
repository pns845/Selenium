from selenium import webdriver
class Findbylink():
    def test(self):
        baseURL="https://learn.letskodeit.com/p/practice"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.get(baseURL)
        element_by_link=driver.find_element_by_link_text("Login")
        if element_by_link is not None:
            print("element found by link text")
        else:
            print("element not found")
        element_by_partial=driver.find_element_by_partial_link_text("Sign")
        if element_by_partial is not None:
            print("element found by partial link text")
        else:
            print("element not found")

c=Findbylink()
c.test()