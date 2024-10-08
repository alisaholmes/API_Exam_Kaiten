import allure

from utils.requests_tools import api_request

# перед запуском укажите id пространства, которое нужно удалить

@allure.tag('API_DELETE')
@allure.feature("Remove_space")
@allure.label('owner', 'alisaholmes')
@allure.story("Space")
@allure.severity(allure.severity_level.CRITICAL)
def test_remove_space(base_url):
    delete = api_request(base_url, endpoint='api/latest/spaces/{space_id}', method="DELETE")
    #assert delete.status_code == 200, "Ожидается статус код 200 при первичном удалении"
    assert delete.status_code == 404, "Ожидается статус код 404 при попытке удалении уже ранее удаленного пространства"
