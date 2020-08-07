from selenium import webdriver
from selenium.webdriver.common.by import By


class Find_By_Name():

    def getChromeDriver(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\chromedriver.exe')
        return driver

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = self.getChromeDriver()
        driver.maximize_window()
        driver.get(baseUrl)


        # element_id = driver.find_element_by_id('name')
        element_id = driver.find_element(By.ID, 'name')
        if element_id != None:
            print('We found the element using id')

        # element_name = driver.find_element_by_name('show-hide')
        element_name = driver.find_element(By.NAME, 'show-hide')
        if element_name != None:
            print('We found the element using name')

        # element_xpath = driver.find_element_by_xpath('.//*[@id="name"]')
        element_xpath = driver.find_element(By.XPATH, './/*[@id="name"]')
        if element_xpath is not None:
            print('We found the element using xpath')

        # element_css = driver.find_element_by_css_selector('#displayed-text')
        element_css = driver.find_element(By.CSS_SELECTOR, '#displayed-text')
        if element_css is not  None:
            print('We have found the element using css')

        # element_linkText = driver.find_element_by_link_text('Login')
        element_linkText = driver.find_element(By.LINK_TEXT, 'Login')
        if element_linkText is not None:
            print('We have found the element using linktext')

        # element_partialLinkText = driver.find_element_by_partial_link_text('Pract')
        element_partialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, 'Pract')
        if element_partialLinkText is not None:
            print('We have found the element using partal link text')

        # element_classname = driver.find_element_by_class_name('displayed-class')
        element_classname = driver.find_element(By.CLASS_NAME, 'displayed-class')
        if element_classname is not None:
            print('We have found the element using class')

        # element_tag = driver.find_element_by_tag_name('h1')
        element_tag = driver.find_element(By.TAG_NAME, 'h1')
        if element_tag is not None:
            print('We have found the element using tag')

        






myobj = Find_By_Name()
myobj.test()




