import pytest
import requests


def test_check_status_code(url, expected_status):
    response = requests.get(url)
    assert response.status_code == int(expected_status)
