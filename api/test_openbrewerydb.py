import requests
import pytest
from api.httpClient import HttpClient

base_url = "https://api.openbrewerydb.org"


def test_get_random_brewery():
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/v1/breweries/random")
    response = response[0]
    id_first_request = response.get("id")

    response = httpclient.get(url=f"{base_url}/v1/breweries/random")
    response = response[0]
    id_second_request = response.get("id")

    assert id_first_request != id_second_request


def test_get_brewery_id():
    brewery_id = "810e0e7c-293a-4e3e-a557-13691d30d399"
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/v1/breweries?by_ids={brewery_id}")
    response = response[0]

    assert response.get("id") == brewery_id
    assert response.get("name")
    assert response.get("street")


@pytest.mark.parametrize("city", ["Moscow", "Fyshwick", "Olathe"])
def test_get_brewery_city(city):
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/v1/breweries?by_city={city}")

    for brewery in response:
        assert brewery.get("id")
        assert brewery.get("city") == city


@pytest.mark.parametrize("country", ["Scotland", "Italy", "Japan"])
def test_get_brewery_country(country):
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/v1/breweries?by_country={country}")

    for brewery in response:
        assert brewery.get("id")
        assert brewery.get("country") == country


@pytest.mark.parametrize("state", ["ACT", "Donegal", "Wicklow"])
def test_get_brewery_state(state):
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/v1/breweries?by_state={state}")

    for brewery in response:
        assert brewery.get("id")
        assert brewery.get("state") == state
