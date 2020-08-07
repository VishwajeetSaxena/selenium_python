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
driver.get(base_url)
driver.implicitly_wait(30)

# radio button
bmw_radio = driver.find_element(By.XPATH, "//input[@id='bmwradio']")
benz_radio = driver.find_element(By.XPATH, "//input[@id='benzradio']")

# checkbox
bmw_checkbox = driver.find_element(By.XPATH, "//input[@id='bmwcheck']")
benz_checkbox = driver.find_element(By.XPATH, "//input[@id='benzcheck']")

'''
Selenium methods and properties to control elements 

To use is_selected and click option on radio and checkbox
'''

# Click radio button and check which one is selected
bmw_radio.click()
benz_radio.click()
print("Is BMW radio button selected: ", bmw_radio.is_selected())
print("Is BENZ radio button selected: ", benz_radio.is_selected())

# Click checkbox and check which one is selected
bmw_checkbox.click()
benz_checkbox.click()
print("Is BMW checkbox selected: ", bmw_checkbox.is_selected())
print("Is BENZ checkbox selected: ", benz_checkbox.is_selected())

driver.quit()