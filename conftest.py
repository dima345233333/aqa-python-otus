import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="http://127.0.0.1",
        help="Request url"
    )
    parser.addoption(
        "--status_code",
        default="200",
        help = "Return status code"
    )
    parser.addoption(
        "--browser",
        default="chrome",
        help="Choose a browser"
    )

    parser.addoption(
        "--base-url",
        default="http://localhost:8081",
        help="Choose a base url"
    )

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def expected_status(request):
    return request.config.getoption("--status_code")

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")

@pytest.fixture
def browser(request):
    browser: str = request.config.getoption("--browser")
    if browser == 'chrome':
        service: Service = Service()
        driver = webdriver.Chrome(service=service)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser {browser} not supported")

    yield driver

    driver.quit()