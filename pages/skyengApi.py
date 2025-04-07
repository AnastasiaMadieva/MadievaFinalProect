import requests
import allure


class SkyengApi:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    @allure.step("Просмотреть события")
    def events_api(self, token: str):
        my_body = {
            'from': '2025-03-21T18:30:00+05:00',
            'till': '2025-03-21T19:00:00+05:00',
            'onlyTypes': []
        }
        my_headers = {}
        my_headers['Cookie'] = token
        resp = requests.post(self.base_url+'events',
                             json=my_body, headers=my_headers)
        return resp.json()

    @allure.step("Добавить событие")
    def createPersonal_api(self, old_title: str, old_color: str, token: str):
        my_body = {
            'backgroundColor': '#F4F5F6',
            'color': old_color,
            'description': '',
            'title': old_title,
            'startAt': '2025-03-21T18:30:00+05:00',
            'endAt': '2025-03-21T19:00:00+05:00'
        }
        my_headers = {}
        my_headers['Cookie'] = token
        resp = requests.post(self.base_url+'createPersonal',
                             json=my_body, headers=my_headers)
        return resp.json()

    @allure.step("Удалить событие ")
    def removePersonal_api(self, taskId: int, token: str):
        my_body = {
            'id': taskId,
            'startAt': '2025-03-21T18:30:00+05:00'
        }
        my_headers = {}
        my_headers['Cookie'] = token
        resp = requests.post(self.base_url+'removePersonal',
                             json=my_body, headers=my_headers)
        return resp.json()

    @allure.step("Редактировать название события ")
    def updatePersonal_title_api(self, taskId: int, new_title: str, token: str):
        my_body = {
            'backgroundColor': '#F4F5F6',
            'color': '#81888D',
            'description': '',
            'title': new_title,
            'startAt': '2025-03-21T18:30:00+05:00',
            'endAt': '2025-03-21T19:00:00+05:00',
            'id': taskId,
            'oldStartAt': '2025-03-21T18:30:00+05:00'
        }
        my_headers = {}
        my_headers['Cookie'] = token
        resp = requests.post(self.base_url+'updatePersonal',
                             json=my_body, headers=my_headers)
        return resp.json()

    @allure.step("Редактировать цвет события ")
    def updatePersonal_color_api(self, taskId: int, new_color: str, token: str):
        my_body = {
            'backgroundColor': '#F4F5F6',
            'color': new_color,
            'description': '',
            'title': 'Личное событие',
            'startAt': '2025-03-21T18:30:00+05:00',
            'endAt': '2025-03-21T19:00:00+05:00',
            'id': taskId,
            'oldStartAt': '2025-03-21T18:30:00+05:00'
        }
        my_headers = {}
        my_headers['Cookie'] = token
        resp = requests.post(self.base_url+'updatePersonal',
                             json=my_body, headers=my_headers)
        return resp.json()
