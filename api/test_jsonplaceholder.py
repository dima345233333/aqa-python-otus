import requests
import pytest

from api.httpClient import HttpClient

base_url = "https://jsonplaceholder.typicode.com"


def test_get_res_jph():
    # response = requests.request(url=f"{base_url}/posts/1", method= "GET")
    # assert response.status_code == 200
    # response_json = response.json()

    httpclient = HttpClient()
    response = httpclient.get(url=f"{base_url}/posts/1")

    assert response.get("userId") == 1
    assert response.get("id") == 1
    assert len(response.get("title")) > 0
    assert len(response.get("body")) > 0


@pytest.mark.parametrize("user_id", ("1", "10", "100"))
def test_create_new_post_jph(user_id):
    data = {"title": "New post", "body": "Data", "userId": user_id}

    httpclient = HttpClient()
    response = httpclient.post(url=f"{base_url}/posts", body=data, code=201)
    assert response["title"] == data["title"]
    assert response["body"] == data["body"]
    assert response["userId"] == data["userId"]
    assert response["id"] is not None


def test_create_post_with_negative_id_jph():
    data = {
        "title": "Negative User Test",
        "body": "Testing with negative userId",
        "userId": "-1",
    }
    httpclient = HttpClient()
    response = httpclient.post(url=f"{base_url}/posts", body=data, code=201)
    assert response["userId"] == "-1"
    assert response["title"] == data["title"]


@pytest.mark.parametrize("user_id, post_id", [(1, 10), (5, 51), (9, 91)])
def test_update_posts_jph(user_id, post_id):
    data = {"title": "Text1", "body": "Text2", "userId": user_id}

    httpclient = HttpClient()
    response = httpclient.put(url=f"{base_url}/posts/{post_id}", body=data)

    assert response["userId"] == str(data.get("userId"))
    assert response["title"] == data.get("title")
    assert response["body"] == data.get("body")


def test_delete_post_jph():
    httpclient = HttpClient()
    response = httpclient.delete(url=f"{base_url}/posts/1")
