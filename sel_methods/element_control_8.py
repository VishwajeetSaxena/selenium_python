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

time.sleep(5)
# Get the collection of elements
page_element_collection = driver.find_elements(By.XPATH, "//*")

'''
Selenium methods and properties to control elements 

To get any attribute
'''
i = 0
for element in page_element_collection:
    # print(cell.text)
    if element.get_attribute('href'):
        i = i + 1
        print('Link#{} : {} with Tag {}'.format(i, element.get_attribute('href'), element.get_attribute('type')))

driver.quit()
