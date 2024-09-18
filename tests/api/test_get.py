import allure

from utils.requests_tools import api_request_authorization, api_request


@allure.tag('API_GET')
@allure.feature("Авторизация")
@allure.label('owner', 'alisaholmes')
@allure.story("Вход зарегистрированного пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_authorization_API(base_url):
    with allure.step("Направить GET запрос на авторизацию"):
        response = api_request_authorization(base_url, method="GET")
        assert response.status_code == 200, "Ожидается статус код 200"


@allure.tag('API_GET')
@allure.feature("Retrieve list of spaces")
@allure.label('owner', 'alisaholmes')
@allure.story("Spaces")
@allure.severity(allure.severity_level.NORMAL)
def test_retrieve_list_of_spaces(base_url):
    with allure.step("Направить GET запрос на retrieve list of spaces"):
        response = api_request(base_url, endpoint='api/latest/spaces', method="GET")
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200, "Ожидается статус код 200"


@allure.tag('API_GET')
@allure.feature("Retrieve space")
@allure.label('owner', 'alisaholmes')
@allure.story("Spaces")
@allure.severity(allure.severity_level.CRITICAL)
def test_retrieve_spaces(base_url):
    with allure.step("Направить GET запрос на Retrieve space"):
        response = api_request(base_url, endpoint="api/latest/spaces/440336", method="GET")
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200, "Ожидается статус код 200"
