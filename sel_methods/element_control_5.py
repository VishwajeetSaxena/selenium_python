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

# radio button collection(list of elements)
dropdown_collection = driver.find_element(By.XPATH, "//select[@id='carselect']")
sel = Select(dropdown_collection)



'''
Selenium methods and properties to control elements 

To use Select method (works only on Select Tag dropdown)
'''
print("Deselect all the options")
# sel.deselect_all()

print("Select by index")
sel.select_by_index(1)
time.sleep(1)
# sel.deselect_by_index(1)

print("Select by value")
sel.select_by_value('bmw')
time.sleep(1)

print("Select by visible text")
sel.select_by_visible_text('Honda')
time.sleep(1)
driver.quit()