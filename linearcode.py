import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

path=r"C:\Users\kundu\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(30)

driver.get("https://www.abhibus.com/")
driver.maximize_window()

'''offers'''
driver.find_element("xpath","//li[(@class='nav-item')]").click()
time.sleep(2)

'''leaving from'''
driver.find_element("xpath","//input[(@type='text')]").send_keys("pune")
time.sleep(2)
driver.find_element("xpath","//li[text()='Pune Airport']").click()

'''going to'''
driver.find_element("xpath","//input[(@name='destination')]").send_keys("Mumbai")
time.sleep(2)
driver.find_element("xpath","//li[text()='Mumbai International Airport']").click()

'''date of jouirney'''
driver.find_element("xpath","//input[(@id='datepicker1')]").click()
driver.find_element("xpath","//a[(@class='ui-state-default')]").click()


