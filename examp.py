from selenium import webdriver
from selenium.webdriver.common.by import By

class Element:
    def __init__(self,driver):
        self.d = driver
    def URL(self,baseURL):
        self.d.get(baseURL)
    def LocatorType(self,locator):
        self.locator=locator.lower()
        if locator=='id':
            return By.ID
        elif locator=='xpath':
            return By.XPATH
    def GetElement(self,proprtyname,locator):
        print("locator is",locator)
        type = self.LocatorType(locator.lower())
        print(type,proprtyname)
        element = driver.find_element(type,proprtyname)
        return element
        #print("path is",path)
    def iselementpresent(self,type,proprtyname):
        element=None

        try:
            element = driver.find_element(type, proprtyname)
            if element is not None:
                print("Element found")
            else:
                print("element not found")
        except:
            print("element is not present")

    def iselementspresent(self, type, proprtyname):
        elements= None
        try:
            elements = driver.find_elements(type, proprtyname)
            if len(elements)>0:
                print("Elements found")
            else:
                print("element not found")
        except:
            print("element is not present")
    def sendkey(self, elements):
        elements.send_keys("testing")
    def close(self):
        self.d.close()



driver = webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
driver.maximize_window()
# driver.get(baseURL)
# time.sleep(3)

e = Element(driver)
e.URL("https://letskodeit.teachable.com/p/practice")
e.LocatorType('id')

elemen = e.GetElement('name','id')
e.iselementpresent('xpath',"//input[@id='name']")
e.iselementspresent('id','nam')
e.sendkey(elemen)
e.close()

# f=Element()
# f.URL("https://www.facebook.com")
