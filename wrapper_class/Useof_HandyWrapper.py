from selenium import webdriver
from wrapper_class.HandyWrapper import HandyWrapper

class Use_of_Handywrapper():

    def method1(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\chromedriver.exe')
        base_url = 'https://letskodeit.teachable.com/p/practice'

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(30)
        handy = HandyWrapper(driver)

        # Get element
        element1 = handy.get_element('xPath', "//input[@id='bmwradio']")
        element1.click()

        # Get element collection
        element_collection = handy.get_elements('Xpath', "//input")
        for element in element_collection:
            if element.get_attribute('type') is not None:
                print('Type of Element: ', element.get_attribute('type'))

        # Get and check if element exist
        element2 = handy.check_element_present('xPath', "//input[@id='benzradio']")
        print('Is element present ', element2)

        # Get and check if element collection exist
        element_collection = handy.check_elements_present('Xpath', "//input")
        print('Are elements present ', element_collection)

        # Get and check if element collection exist
        # element3 = handy.wait_until_element_present('By.Xpath', "//input[@id='benzradio']", "click")
        element3 = handy.wait_until_element_present('xpath', "//input[@id='displayed-text']", 'click')
        print('Are elements present ', element3)

        #Take Screenshot
        handy.take_screenshot()

        driver.quit()

test = Use_of_Handywrapper()
test.method1()
