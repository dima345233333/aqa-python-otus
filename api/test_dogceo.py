import json
import requests
import pytest
from api.httpClient import HttpClient

base_url = "https://dog.ceo"


def is_image(image_url: str) -> bool:
    response_image = requests.request("GET", image_url)
    if response_image.status_code != 200:
        return False
    if not "image" in response_image.headers.get("Content-Type", ""):
        return False
    if int(response_image.headers.get("Content-Length", "")) == 0:
        return False
    return True


def test_get_all_breeds():
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/api/breeds/list/all")

    with open("api/breeds.json", "r", encoding="utf-8") as file_breeds:
        breeds = json.load(file_breeds)
    assert breeds == response.get("message")
    assert response.get("status") == "success"


def test_get_random_image_from_all_dogs_collection():
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/api/breeds/image/random")

    assert response.get("status") == "success"
    assert "https://images.dog.ceo/breeds/" in response.get("message")

    url_image = response.get("message")
    assert is_image(url_image) == True


@pytest.mark.parametrize("count", [1, 5, 10])
def test_get_multiple_random_image_from_all_dogs_collection(count):
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/api/breeds/image/random/{count}")

    assert response.get("status") == "success"
    url_images = response.get("message")
    for single_url in url_images:
        assert is_image(single_url) == True


def test_get_hound():
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/api/breed/hound/images/random")

    assert response.get("status") == "success"
    assert "https://images.dog.ceo/breeds/hound" in response.get("message")
    assert is_image(response.get("message")) == True


@pytest.mark.parametrize("breed", ["airedale", "buhund", "corgi"])
def test_get_several_breed(breed):
    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/api/breed/{breed}/images/random")

    assert response.get("status") == "success"
    assert f"https://images.dog.ceo/breeds/{breed}" in response.get("message")
    assert is_image(response.get("message")) == True
