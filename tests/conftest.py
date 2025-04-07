import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from tests.dataProvider import DataProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def ui_phone():
    phone = DataProvider().get_phone()
    return phone


@pytest.fixture
def ui_passw():
    password = DataProvider().get_passw()
    return password

