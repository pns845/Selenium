from selenium import webdriver
class FindbyClassTag():
    baseURL="https://learn.letskodeit.com/p/practice"
    driver=webdriver.Chrome(executable_path="C:\\Users\\M524891\\PycharmProjects\\workspace_python\\drivers\\chromedriver.exe")
    driver.get(baseURL)
    element_class=driver.find_element_by_class_name("inputs")
    element_class.send_keys("hey")
    element_classn = driver.find_element_by_class_name("displayed-class")
    element_classn.send_keys("hey")
    if element_class is not None:
        print("element found by using class name")
    else:
        print("element not found")
    element_tag=driver.find_element_by_tag_name("h1")
    text=element_tag.text
    print(text)
   # element_tag.click()
    if element_tag is not None:
        print("element found by using tag name")
    else:
        print("element not found")
