import time

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
driver.get('https://www.google.com/')
driver.implicitly_wait(30)

# navigate to login page
element_with_disable_attribute = driver.find_element(By.XPATH, "//input[@name='iflsig']")
# user name
element_with_no_disable_attribute = driver.find_element(By.XPATH, '//input[@class=\'gLFyf gsfi\']')

'''
Selenium methods and properties to control elements 

To see if the element is enabled 
(as many elements contains disable attribute and cause run time exception)
'''

# Check the first element enable state
element1_state = element_with_disable_attribute.is_enabled()
print('Element1 state: ', element1_state)

# Check the second element enable state
element2_state = element_with_no_disable_attribute.is_enabled()
print('Element1 state: ', element2_state)

driver.quit()
