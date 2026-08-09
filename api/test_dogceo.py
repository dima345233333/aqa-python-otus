import json
import requests
import pytest

base_url = "https://dog.ceo"

def is_image (image_url: str) -> bool:
    response_image = requests.request("GET", image_url)
    if response_image.status_code != 200:
        return False
    if not "image" in response_image.headers.get('Content-Type', ''):
        return False
    if int(response_image.headers.get('Content-Length', '')) == 0:
        return False
    return True

def test_get_all_breeds():
    response = requests.request("GET", f"{base_url}/api/breeds/list/all")
    assert response.status_code == 200

    response_json = response.json()
    with open("api/breeds.json", "r", encoding="utf-8") as file_breeds:
        breeds = json.load(file_breeds)
    assert breeds == response_json.get("message")

    assert response_json.get("status") == "success"

def test_get_random_image_from_all_dogs_collection():
    response = requests.request("GET", f"{base_url}/api/breeds/image/random")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get("status") == "success"
    assert "https://images.dog.ceo/breeds/" in response_json.get("message")

    url_image = response_json.get("message")
    assert is_image(url_image) == True

@pytest.mark.parametrize("count", [1,5,10])
def test_get_multiple_random_image_from_all_dogs_collection(count):
    response = requests.request("GET", f"{base_url}/api/breeds/image/random/{count}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get("status") == "success"
    url_images = response_json.get("message")
    for single_url in url_images:
        assert is_image(single_url) == True

def test_get_hound():
    response = requests.request("GET", f"{base_url}/api/breed/hound/images/random")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get("status") == "success"
    assert "https://images.dog.ceo/breeds/hound" in response_json.get("message")
    assert is_image(response_json.get("message")) == True

@pytest.mark.parametrize("breed", ["airedale","buhund","corgi"])
def test_get_several_breed(breed):
    response = requests.request("GET", f"{base_url}/api/breed/{breed}/images/random")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get("status") == "success"
    assert f"https://images.dog.ceo/breeds/{breed}" in response_json.get("message")
    assert is_image(response_json.get("message")) == True