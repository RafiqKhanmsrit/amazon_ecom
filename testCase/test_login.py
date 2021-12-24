import pytest
import xdist
import pytest
from selenium import webdriver
from pageobjects.LoginClass import LoginPage
from utilities.properyFiles import ConfigFile
from testCase.conftest import *
from utilities.logconfi import Loggen


class TestLogin:
    url = ConfigFile.geturl()
    userid = ConfigFile.geuserid()
    password = ConfigFile.getpassword()
    @pytest.mark.regression
    def test_login(self, setup):
        Loggen.loggen().warning("hello im fine ")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.click_sigin_account()
        self.lp.send_user_id(self.userid)
        self.lp.click_continue()
        self.lp.send_password(self.password)
        Loggen.loggen().warning("hello im fine ")
        self.lp.click_sign_in()
        if self.driver.title == "Amazon Sign-In":
            assert True
            Loggen.loggen().warning("hello im fine ")
        else:
            Loggen.loggen().warning("hello im fine ")
            self.driver.save_screenshot("C:\\Users\\B24\\PycharmProjects\\ecom\\screentshots\\login2Test.jpg")
            assert False
    @pytest.mark.sanity
    def test_homepage(self, setup):
        Loggen.loggen().warning("testing home page started  ")
        self.driver = setup
        self.driver.get(self.url)
        if self.driver.title=="Amazon.com. Spend less. Smile more.":
            assert True
        else:
            assert False