import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDriver():

    def getChromeDriver(self):
        chrome_driver = webdriver.Chrome(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\chromedriver.exe')
        return chrome_driver

base_url = 'https://letskodeit.teachable.com/p/practice'
# Get a browser instance
sel_chrome_driver = SeleniumDriver()
driver = sel_chrome_driver.getChromeDriver()
driver.maximize_window()
driver.get(base_url)

'''
Selenium implicit wait 

'''
# Put implicit wait, which will apply to all the elements
driver.implicitly_wait(30)

# Get an element
element = driver.find_element(By.XPATH, "//input[@id='bmwradio']")
element.click()

driver.quit()
