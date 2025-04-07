from pages.skyengApi import SkyengApi
from tests.dataProvider import DataProvider
import allure


api = SkyengApi("https://api-teachers.skyeng.ru/v2/schedule/")
old_color = '#81888D'
new_color = '#D478F1'
old_title = "Старое название события"
new_title = 'Новое название события'
token = 'token_global=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0ODk0MjUwLCJpZGVudGl0eSI6InRlc3QudHN0MzQ1QHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5MTY1MDAyMjU1IiwibmFtZSI6Ilx1MDQxMFx1MDQzYlx1MDQzNVx1MDQzYVx1MDQ0MVx1MDQzNVx1MDQzOSIsInN1cm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6ImVzbVdVc1BSRVMzdTlrS1JoR3V1c0czcFpNMEowcTdpIiwiYnJhbmQiOm51bGwsImV4cCI6MTc0NDEyOTg2OCwiYmlydGhkYXkiOiIyMDA2LTEwLTEwIiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NDM4NzE5ODUsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1RFQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xFX0NSTTJfVEVBQ0hFUl9BQ0NFU1MiLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.ezznGYSN3-VgkyMOFfQ6EGKKcRqC0I6kVR_DK3gss-9S5mxeCoHm9qR0j7M4-vfz-hdh2y2xWHLwwwcEUq657SOb5jtzIK3ux3bOid4JxmFAuK-HuwE3MCf2eP7hgwzYpORMv-TJYzT3MJtetrWEa2WSWcURKzBVb98Z2Nb-f0if_jzoQ4YehAy6IDRszduoA7O1TpAW_mT9qhtf7jHDSNEIAXdezFNBCsIJZrp-4QCYbfWXlHsFGvEH24pW6mO9-6ZGLmUasxCebzXSQXtpgA35JFN7cAaXrX79gyajheTFHtjkZUi_H-5jB2XDNrly2_az44MsKwanQEcyTG7lt1OgBzb6D4vg6toMfxWYgbmTKr2OphcvK_c1R5k6tXIfySDe5l01VSmgjKtcJ60h3-uJaRryWDpe95sFbpAXTqHqoNxVouJbsgiMcWbx8eSAwM07pmawWmiaGcSR9UjtmOHFb_TUDdS6RnznYu6cMhWKYqdQpypG7XnQh-Eihy283s1sNe53fmyBeK154i2-_tGoUgdPvyG-d_r44kwoke1LveKhcAR2qifV_MfXEN0BQLh5Q0H63Di-AUchjUJ-CaYXcHHH8cTI5PAWxP4ozi86hffJqco7M2g8ejUPCMH7KKNgBUzcvTgpw7RPBHVNaMOHSxfTN5qzlopDgSxOK70'
token = DataProvider().get_token()

@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-1")
@allure.title("Тестирование просмотра событий api")
@allure.feature("Тестирование просмотра событий api")
@allure.story("Проверка просмотра событий api")
@allure.severity("blocker")
def test_events_api():
    resp_body = api.events_api(token)
    assert len(resp_body) > 0


@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-2")
@allure.title("Тестирование добавления события api")
@allure.feature("Тестирование добавления события api")
@allure.story("Проверка добавления события api")
@allure.severity("blocker")
def test_createPersonal_api():
    with allure.step('Получить список событий до'):
        body = api.events_api(token)
        len_before = len(body['data']['events'])
    task = api.createPersonal_api(old_title, old_color, token)
    taskId = task['data']['payload']['id']
    with allure.step('Получить список событий после'):
        body = api.events_api(token)
        len_after = len(body['data']['events'])
    with allure.step('Почистить за собой'):
        api.removePersonal_api(taskId, token)
    with allure.step('Сравнить, что длина списка событий после добавления больше на 1 списка событий до'):
        assert len_after-len_before == 1


@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-3")
@allure.title("Тестирование удаления события api")
@allure.feature("Тестирование удаления события api")
@allure.story("Проверка удаления события api")
@allure.severity("blocker")
def test_removePersonal_api():
    with allure.step('Получить список событий до'):
        body = api.events_api(token)
        len_before = len(body['data']['events'])
    with allure.step("Получить ID события"):
        task = api.createPersonal_api(old_title, old_color, token)
        taskId = task['data']['payload']['id']
    api.removePersonal_api(taskId, token)
    with allure.step('Получить список событий после'):
        body = api.events_api(token)
        len_after = len(body['data']['events'])
    with allure.step('Сравнить, что длина списка событий после равна списку событий до'):
        assert len_after == len_before


@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-4")
@allure.title("Тестирование редактирования названия события api")
@allure.feature("Тестирование редактирования названия события api")
@allure.story("Проверка редактирования названия события api")
@allure.severity("blocker")
def test_updatePersonal_title_api():
    with allure.step('Получить список событий до'):
        body = api.events_api(token)
        len_before = len(body['data']['events'])
    with allure.step("Получить ID события"):
        task = api.createPersonal_api(old_title, old_color, token)
        taskId = task['data']['payload']['id']
    new_taskTitle = api.updatePersonal_title_api(taskId, new_title, token)
    with allure.step('Получить список событий после'):
        body = api.events_api(token)
        len_after = len(body['data']['events'])
    with allure.step('Почистить за собой'):
        api.removePersonal_api(taskId, token)
    with allure.step('Сравнить, что длина списка событий после добавления и редактирования события больше списка событий до на 1'):
        assert len_after-len_before == 1
    with allure.step(f'Новое название события с ID {taskId} равно {new_title}'):
        assert new_taskTitle['data']['payload']['payload']['title'] == new_title


@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-5")
@allure.title("Тестирование редактирования цвета события по ID события api")
@allure.feature("Тестирование редактирования цвета события по ID api")
@allure.story("Проверка редактирования цвета события по ID api")
@allure.severity("blocker")
def test_updatePersonal_color_api():
    with allure.step('Получить список событий до'):
        body = api.events_api(token)
        len_before = len(body['data']['events'])
    task = api.createPersonal_api(old_title, old_color, token)
    with allure.step('Получить ID'):
        taskId = task['data']['payload']['id']
    new_taskColor = api.updatePersonal_color_api(taskId, new_color, token)
    with allure.step('Получить список событий после'):
        body = api.events_api(token)
        len_after = len(body['data']['events'])
    with allure.step('Почистить за собой'):
        api.removePersonal_api(taskId, token)
    with allure.step('Сравнить, что длина списка событий после добавления больше на 1 списка событий до'):
        assert len_after-len_before == 1
    with allure.step(f'Новый цвет события {taskId} равен {new_color}'):
        assert new_taskColor['data']['payload']['payload']['color'] == new_color
