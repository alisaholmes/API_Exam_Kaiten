import json

import allure
from jsonschema import validate

from utils.requests_tools import api_request
from utils.resource import path

schema_create_space = path('create_space.json')
schema_create_board = path('create_board.json')


@allure.tag('API_POST')
@allure.feature("Create_space")
@allure.label('owner', 'alisaholmes')
@allure.story("Spaces")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_space(base_url):
    payload_create_space = '{ "title": "test", "external_id": 1}'
    with allure.step("Направить POST запрос на создание нового пространства"):
        response = api_request(base_url, endpoint='api/latest/spaces', method="POST", data=payload_create_space)
        body = response.json()
    with allure.step("Проверка результатов"):
        assert response.status_code == 200
        assert response.json()['title'] == 'test'
    with open(schema_create_space) as file:
        f = file.read()
        validate(body, schema=json.loads(f))


@allure.tag('API_POST')
@allure.feature("Create_board")
@allure.label('owner', 'alisaholmes')
@allure.story("Board")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_board(base_url):
    payload_create_board = ('{ "title": "autotest", "columns": [], "lanes": [], "description": "test",'
                            ' "top": 1, "left": 1, "default_card_type_id": 1, "first_image_is_cover": false, '
                            '"reset_lane_spent_time": false, "automove_cards": false, '
                            '"backward_moves_enabled": false, "auto_assign_enabled": false, '
                            '"sort_order": 1, "external_id": 1}')
    with allure.step("Направить POST запрос на создание новой доски"):
        response = api_request(base_url, endpoint='api/latest/spaces/440336/boards', method="POST",
                               data=payload_create_board)
        body = response.json()
    with allure.step("Проверка результатов"):
        assert response.status_code == 200
        assert response.json()['title'] == 'autotest'
    with open(schema_create_board) as file:
        f = file.read()
        validate(body, schema=json.loads(f))
