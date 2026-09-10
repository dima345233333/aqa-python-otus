import pytest
import requests

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

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def expected_status(request):
    return request.config.getoption("--status_code")
