from asyncio import timeout

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from configuration.ConfigProvider import ConfigProvider
from test_data.DataProvider import DataProvider

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        time_out = ConfigProvider().getint("ui", "timeout")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager()
                                                   .install()))
        browser.implicitly_wait(time_out)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def base_url():
    return ConfigProvider().get( "api", "base_url")


@pytest.fixture
def token():
    return DataProvider().get_token()


@pytest.fixture
def api_key():
    return DataProvider().get_api_key()
    return "91ba4fba5f7264b7f159a057d38fc783"


@pytest.fixture
def org_id():
    return DataProvider().get("org_id")

@pytest.fixture
def test_data():
    return DataProvider()
