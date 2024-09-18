import os

import requests

from utils.attach import response_logging, response_attaching


def api_request_authorization(base_url, method, json=None, params=None):
    headers2 = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {os.getenv('API_TOKEN')}"}

    response = requests.request(method, base_url, json=json, params=params, headers=headers2)
    response_logging(response)
    response_attaching(response)
    return response


def api_request(base_url, endpoint, method, data=None, params=None):
    url = f"{base_url}{endpoint}"
    headers2 = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {os.getenv('API_TOKEN')}"}

    response = requests.request(method, url, data=data, params=params, headers=headers2)
    response_logging(response)
    response_attaching(response)
    return response
