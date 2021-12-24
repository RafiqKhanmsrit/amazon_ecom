import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge(executable_path="C:\Raf_kha\Drivers\edgedriver_win64\msedgedriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
######################  HTML REPORT ######################

def pytes_configure(config):
    config._metadata['project Name'] = "ecom"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Plugins",None)
