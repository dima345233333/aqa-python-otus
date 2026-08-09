from http.client import responses

import requests


class HttpClient:
    
    def request(self, method: str, url: str, body: dict = None, code: int = None, headers: dict = None):
        response = requests.request(method,
                                    url,
                                    headers=headers,
                                    data=body)

        response_json = response.json()
        assert response.status_code == code
        return response_json

    def get(self, url, code: int = 200):
        return self.request(method = "GET", url=url, code = code)