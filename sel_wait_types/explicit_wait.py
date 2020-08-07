import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *

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

'''
Selenium Explicit wait

'''
# Define the wait characteristics
wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
# Apply wait on an element
hidden_element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='displayed-text']")))

show_button = driver.find_element(By.XPATH, "//input[@id='show-textbox']")
hide_button = driver.find_element(By.XPATH, "//input[@id='hide-textbox']")


hide_button.click()

show_button.click()

hidden_element.click()

driver.quit()
