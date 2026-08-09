import requests
import pytest

from api.httpClient import HttpClient

base_url = "https://jsonplaceholder.typicode.com"

def test_get_res_jph():
    #response = requests.request(url=f"{base_url}/posts/1", method= "GET")
    #assert response.status_code == 200
    #response_json = response.json()

    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/posts/1")

    assert response.get("userId") == 1
    assert response.get("id") == 1
    assert len(response.get("title")) > 0
    assert len(response.get("body")) > 0


@pytest.mark.parametrize("user_id", (1,10,100))
def test_create_new_post_jph(user_id):
    data = {
        "title": "New post",
        "body": "Data",
        "userId": user_id
    }

    response = requests.request(method= "POST", url=f"{base_url}/posts", json=data)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["title"] == data["title"]
    assert response_json["body"] == data["body"]
    assert response_json["userId"] == data["userId"]
    assert response_json["id"] is not None


def test_create_post_with_negative_id_jph():
    data = {
        "title": "Negative User Test",
        "body": "Testing with negative userId",
        "userId": -1
    }

    response = requests.post(f"{base_url}/posts", json=data)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["userId"] == -1
    assert response_json["title"] == data["title"]

@pytest.mark.parametrize("user_id, post_id", [(1,10),(50,51),(90,91)])
def test_update_posts_jph(user_id,post_id):
    data = {
        "title": "Text1",
        "body": "Text2",
        "userId": user_id
    }

    response = requests.request(method="PUT", url=f"{base_url}/posts/{post_id}", json=data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["userId"] == data.get("userId")
    assert response_json["title"] == data.get("title")
    assert response_json["body"] == data.get("body")


def test_delete_post_jph():
    response = requests.request(url=f"{base_url}/posts/1", method= "DELETE")
    assert response.status_code == 200





