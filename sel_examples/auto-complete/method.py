from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.southwest.com"
        driver = webdriver.Chrome(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\chromedriver.exe')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        cityField = driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
        cityField.send_keys("New York")
        time.sleep(3)
        # Find the item and click
        # itemToSelect = driver.find_element_by_xpath("//ul[@id='air-city-departure-menu']//li[contains(text(),'NJ - EWR')]")
        itemToSelect = driver.find_elements_by_xpath("//ul//button")

        # print(driver.page_source)
        for i in itemToSelect:
            # print(i.text)
            if i.text == 'New York (LaGuardia), NY - LGA':
                i.click()
                break


        time.sleep(10)
        driver.quit()

temp = CalendarSelection()
temp.test1()
