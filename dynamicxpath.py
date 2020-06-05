from selenium import webdriver
import time

class Driver():
    def driver(self):
        baseURL = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)
        #Login=driver.find_element_by_xpath("//a[@href='/sign_in']")
        Login=driver.find_element_by_link_text("Login")
        Login.click()

        userName=driver.find_element_by_id("user_email")
        userName.send_keys("test@email.com")
        time.sleep(3)
        password=driver.find_element_by_id("user_password")
        password.send_keys("abcabc")
        time.sleep(3)
        Loginbu = driver.find_element_by_name("commit")
        Loginbu.click()
        searchBox=driver.find_element_by_id("search-courses")
        searchBox.send_keys("JavaScript")
        time.sleep(3)
        driver.find_element_by_id("search-course-button").click()
        time.sleep(3)
        #ele=driver.find_element_by_xpath("//div[contains(@class,'course-listing-title') and contains(text(),'JavaScript for beginners')]")
        #to selecct any text the syntax is as below
        _course="//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator=_course.format("JavaScript for beginners")
        courseelement=driver.find_element_by_xpath(_courseLocator)
        courseelement.click()
        time.sleep(3)


d=Driver()
d.driver()