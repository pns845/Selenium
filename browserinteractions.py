from selenium import webdriver
class browserInteractions():
    def test(self):
        baseURL="http://wa1dndbs001/ContractManagementDev/"
        driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        title_page=driver.title
        print("title of web page is:"+title_page)
        currentURL=driver.current_url
        print("the current url is:"+currentURL)
        driver.refresh()
        driver.get(currentURL)
        driver.get("http://www.google.com")
        driver.back()
        driver.forward()
        #driver.close()
        driver.quit()
ch=browserInteractions()
ch.test()

