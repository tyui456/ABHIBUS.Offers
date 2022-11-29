import time
# from selenium import webdriver
# path = r"C:\Users\kundu\Downloads\chromedriver_win32\chromedriver.exe"
#
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://www.abhibus.com/")
# driver.maximize_window()


class offerpage:
    def __init__(self,driver):
        self.driver=driver

    def click_offer(self):
        self.driver.find_element("xpath","//li[(@class='nav-item')]").click()
        time.sleep(2)

    def click_leavingfrom(self):
        self.driver.find_element("xpath", "//input[(@type='text')]").send_keys("pune")
        time.sleep(2)
        self.driver.find_element("xpath", "//li[text()='Pune Airport']").click()

    def click_goingto(self):
        self.driver.find_element("xpath", "//input[(@name='destination')]").send_keys("Mumbai")
        time.sleep(2)
        self.driver.find_element("xpath", "//li[text()='Mumbai International Airport']").click()

    def click_datetojourney(self):
        self.driver.find_element("xpath", "//input[(@id='datepicker1')]").click()
        self.driver.find_element("xpath", "//a[(@class='ui-state-default')]").click()

# obj=offerpage(driver)
# obj.click_offer()
# obj.click_leavingfrom()
# obj.click_goingto()
# obj.click_datetojourney()





