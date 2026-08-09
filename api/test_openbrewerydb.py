import requests
import pytest

base_url = "https://api.openbrewerydb.org"

def test_get_random_brewery():
    response = requests.request(method="GET", url=f"{base_url}/v1/breweries/random")
    assert response.status_code == 200
    response_json = response.json()[0]
    id_first_request = response_json.get("id")

    response = requests.request(method="GET", url=f"{base_url}/v1/breweries/random")
    assert response.status_code == 200
    response_json = response.json()[0]
    id_second_request = response_json.get("id")

    assert id_first_request != id_second_request

def test_get_brewery_id():
    brewery_id = "810e0e7c-293a-4e3e-a557-13691d30d399"
    response = requests.request(method="GET", url=f"{base_url}/v1/breweries?by_ids={brewery_id}")

    assert response.status_code == 200
    response_json = response.json()[0]
    assert response_json.get("id") == brewery_id
    assert response_json.get("name")
    assert response_json.get("street")

@pytest.mark.parametrize("city", ["Moscow", "Fyshwick", "Olathe"])
def test_get_brewery_city(city):
    response = requests.request(method="GET", url=f"{base_url}/v1/breweries?by_city={city}")
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery.get("id")
        assert brewery.get("city") == city

@pytest.mark.parametrize("country", ["Scotland", "Italy", "Japan"])
def test_get_brewery_country(country):
    response = requests.request(method="GET", url=f"{base_url}/v1/breweries?by_country={country}")

    assert response.status_code == 200
    for brewery in response.json():
        assert brewery.get("id")
        assert brewery.get("country") == country


@pytest.mark.parametrize("state", ["ACT", "Donegal", "Wicklow"])
def test_get_brewery_state(state):
    response = requests.request(method="GET", url=f"{base_url}/v1/breweries?by_state={state}")

    assert response.status_code == 200
    for brewery in response.json():
        assert brewery.get("id")
        assert brewery.get("state") == state
