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
driver.implicitly_wait(30)

# Check if an element is displayed(only works if element is present in the DOM, else give the exception)
hidden_element = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
show_button = driver.find_element(By.XPATH, "//input[@id='show-textbox']")
hide_button = driver.find_element(By.XPATH, "//input[@id='hide-textbox']")

'''
Selenium methods and properties to control elements 

To use is_displayed method to check if an element is displayed
(only works if element is present in the DOM, else give the exception)
'''
if hidden_element is not None:
    print("Element is present in the DOM")

show_button.click()
print("After clicking show: ")
print("Is element is displayed", hidden_element.is_displayed())

hide_button.click()
print("After clicking hide: ")
print("Is element is displayed", hidden_element.is_displayed())

driver.quit()
