from selenium import webdriver

class SeleniumDriver():

    def getChromeDriver(self):
        chrome_driver = webdriver.Chrome(executable_path='C:\\Users\\91897\\workspace_python\\sel_drivers\\chromedriver.exe')
        return chrome_driver


base_url = 'https://letskodeit.teachable.com/p/practice'

# Get a browser instance
sel_chrome_driver = SeleniumDriver()
driver = sel_chrome_driver.getChromeDriver()

'''
Selenium methods and properties to control browser 
'''
# Maximize browser window
print('Maximize the browser')
driver.maximize_window()

# Open a Url
print('Open the browser url')
driver.get('https://letskodeit.com/')

# Get the title of the page (using page title property)
print('Get the page title')
page_title = driver.title
print('Page title: ', page_title)

# Get current Url of the webpage
print('Get the current url')
current_url = driver.current_url
print('Url of the current page: ', current_url)

# Get webpage refresh
print('Refresh the browser')
driver.refresh()

# Get the webpage back to previous page
new_url = 'https://letskodeit.teachable.com/'
driver.get(new_url)
print('Back the browser to previous page')
driver.back()

# Get the webpage forward
print('Forward the browser to previous page')
driver.forward()

# Get the page source
print('Get the page source')
page_source = driver.page_source
print('Page Source :')
print(page_source)

# Close the browser single window
# print('Close the browser')
# driver.close()

# Quit all the windows of the browser
print('Quit all windows of the browser')
driver.quit()
