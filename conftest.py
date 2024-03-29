# coding=utf-8
import pytest
from selenium import webdriver
import os

#Get browser name from arguments, use parser as it is
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Type in Your Browser Name e.g chrome,Firefox")

#conftest is used to have the fixtures in one place, so this portion was in login_test.py
# just added request param, from selenium import webdriver and request.cls.driver = driver
@pytest.fixture(scope='class')
def test_setup(request):
    browser = request.config.getoption("--browser")
    #driver_path = os.path.join(os.getcwd(),"venv\\Script")

    if browser =="chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(15)
    driver.maximize_window()
    # next line will sent the driver variable to the class
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test complete")