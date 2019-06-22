
import pytest


from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as env

#to link the setup in conftest.py
@pytest.mark.usefixtures("test_setup")

class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(env.URL)
        casename = env.whoami()
        login = LoginPage(driver)
        login.enter_username(env.USERNAME)
        login.enter_password(env.PASSWORD)
        env.screenshot(self,casename)
        login.click_login()

    def test_logout(self):
        driver = self.driver
        casename = env.whoami()
        try:
            homepage = HomePage(driver)
            driver.implicitly_wait(15)
            env.screenshot(self, casename)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRM"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            env.screenshot(self,casename)
            raise
        except:
            print("There was an exception")
            env.screenshot(self,casename)
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("Inside finally block")




