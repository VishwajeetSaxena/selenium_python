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

# Get the collection of elements
table_cell_collection = driver.find_elements(By.XPATH, "//table//td")

'''
Selenium methods and properties to control elements 

To get text attribute
'''
for cell in table_cell_collection:
    # print(cell.text)
    if 'Python' in str(cell.text):
        print('The cell we are searching has been found, it is: ', cell.text)
        break

driver.quit()
