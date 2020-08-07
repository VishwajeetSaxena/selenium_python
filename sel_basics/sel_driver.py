from selenium import webdriver

class SeleniumDriver():

    def getFirefoxDriver(self):
        ff_driver = webdriver.Firefox(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\geckodriver.exe')
        ff_driver.get('https://letskodeit.com/')
        ff_driver.close()

    def getChromeDriver(self):
        chrome_driver = webdriver.Chrome(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\chromedriver.exe')
        chrome_driver.get('https://letskodeit.com/')
        chrome_driver.close()

    def getIEDriver(self):
        ie_driver = webdriver.Ie(
            executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\IEDriverServer.exe')
        ie_driver.get('https://letskodeit.com/')
        ie_driver.close()


    def getEdgeDriver(self):
        edge_driver = webdriver.Edge(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\msedgedriver.exe')
        edge_driver.get('https://letskodeit.com/')
        edge_driver.close()
        # edge_driver.quit()




#Firefox
sel_ff_driver = SeleniumDriver()
sel_ff_driver.getFirefoxDriver()

#Chrome
sel_chrome_driver = SeleniumDriver()
sel_chrome_driver.getChromeDriver()

#Edge browser
sel_edge_driver = SeleniumDriver()
sel_edge_driver.getEdgeDriver()

#Internet Explorer
sel_ie_driver = SeleniumDriver()
sel_ie_driver.getIEDriver()
