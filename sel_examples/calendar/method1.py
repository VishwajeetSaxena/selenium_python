from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\chromedriver.exe')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Find departing field
        departingField = driver.find_element_by_id("d1-btn")
        # Click departing field
        departingField.click()
        # Find the date to be selected
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        dateToSelect = driver.find_element(By.XPATH,"//div[@class='uitk-new-date-picker-desktop-months-container']/div[1]//tbody//td/button[@data-day='5']")

        # Click the date
        dateToSelect.click()

        time.sleep(3)
        driver.quit()

temp = CalendarSelection()
temp.test1()
