import pytest
from selenium import webdriver
from library.config import Config
from selenium.webdriver.firefox.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

firefox_Driver_path =r"C:\Users\kundu\Downloads\geckodriver-v0.32.0-win64\geckodriver.exe"
@pytest.fixture(params=["Firefox","Chrome","Edge"])
# def _driver():
#     driver=webdriver.Chrome(executable_path=path)
#     driver.get("https://www.abhibus.com/")
#     driver.maximize_window()
#     yield driver

def _driver(request):
    if request.param == "Firefox":
        option = Options()
        option.binary_location =r'C:\program files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=Config.firefox_Driver_path,options=option)

    elif request.param == "Chrome":
        driver = webdriver.Chrome(executable_path=Config.Chrome_Driver_path)

    elif request.param == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    print(driver.title)
    driver.save_screenshot("test.offerpage")
    driver.close()







