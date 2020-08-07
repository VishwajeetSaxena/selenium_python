from selenium import webdriver


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
        element_id = driver.find_elements_by_id('name')
        if element_id != None:
            print('We found the element using id')
            print('number of elements =', len(element_id))

        # element_name = driver.find_element_by_name('show-hide')
        element_name = driver.find_elements_by_name('show-hide')
        if element_name != None:
            print('We found the element using name')
            print('number of elements =', len(element_name))

        # element_xpath = driver.find_element_by_xpath('.//*[@id="name"]')
        element_xpath = driver.find_elements_by_xpath('.//*[@id="name"]')
        if element_xpath is not None:
            print('We found the element using xpath')
            print('number of elements =', len(element_xpath))

        # element_css = driver.find_element_by_css_selector('#displayed-text')
        element_css = driver.find_elements_by_css_selector('#displayed-text')
        if element_css is not  None:
            print('We have found the element using css')
            print('number of elements =', len(element_css))

        # element_linkText = driver.find_element_by_link_text('Login')
        element_linkText = driver.find_elements_by_link_text('Login')
        if element_linkText is not None:
            print('We have found the element using linktext')
            print('number of elements =', len(element_linkText))

        # element_partialLinkText = driver.find_element_by_partial_link_text('Pract')
        element_partialLinkText = driver.find_elements_by_partial_link_text('Pract')
        if element_partialLinkText is not None:
            print('We have found the element using partal link text')
            print('number of elements =', len(element_partialLinkText))

        # element_classname = driver.find_element_by_class_name('displayed-class')
        element_classname = driver.find_elements_by_class_name('displayed-class')
        if element_classname is not None:
            print('We have found the element using class')
            print('number of elements =', len(element_classname))

        # element_tag = driver.find_element_by_tag_name('h1')
        element_tag = driver.find_elements_by_tag_name('a')
        if element_tag is not None:
            print('We have found the element using tag')
            print('number of elements =', len(element_tag))








myobj = Find_By_Name()
myobj.test()




