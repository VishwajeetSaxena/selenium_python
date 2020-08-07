import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumDriver():

    def getChromeDriver(self):
        chrome_driver = webdriver.Chrome(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\chromedriver.exe')
        return chrome_driver

base_url = 'https://letskodeit.com/'
# Get a browser instance
sel_chrome_driver = SeleniumDriver()
driver = sel_chrome_driver.getChromeDriver()
driver.maximize_window()
driver.get(base_url)
driver.implicitly_wait(30)

# navigate to login page
login_link = driver.find_element(By.XPATH, '//a[@href=\'/sign_in\']')
# user name
user_name = driver.find_element(By.XPATH, '//input[@id=\'user_email\']')
# user password
password = driver.find_element(By.XPATH, '//input[@id=\'user_password\']')

'''
Selenium methods and properties to control elements 
'''

# Click an element
login_link.click()

# Clear a text box element
user_name.clear()
password.clear()

time.sleep(2)

# Send the data to a textbox element
user_name.send_keys('test user name')
password.send_keys('test password')
