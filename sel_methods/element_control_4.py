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

# radio button collection(list of elements)
radio_collection = driver.find_elements(By.XPATH, "//fieldset//input[@type='radio']")


'''
Selenium methods and properties to control elements 

To use collection of elements
'''
print("Number of elements in the radio collections are: ", len(radio_collection))
for radio in radio_collection:
    isSelected = radio.is_selected()
    if not isSelected:
        radio.click()
        time.sleep(1)

driver.quit()