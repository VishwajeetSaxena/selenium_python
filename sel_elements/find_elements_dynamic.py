import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Find_By_Name():

    def getChromeDriver(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\chromedriver.exe')
        return driver

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/courses'
        driver = self.getChromeDriver()
        driver.maximize_window()
        driver.get(baseUrl)

        # construct dynamic xpath
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        course_element = driver.find_element(By.XPATH, _courseLocator)
        course_element.click()
        time.sleep(2)


myobj = Find_By_Name()
myobj.test()
