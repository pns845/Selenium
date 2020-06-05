from selenium import webdriver
class Iepractise():
    def test(self):
        driver=webdriver.Ie(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\IEDriverServer.exe")
        driver.get("http://www.guru99.com")

ie=Iepractise()
ie.test()