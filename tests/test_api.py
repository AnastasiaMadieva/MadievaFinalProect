from pages.skyengApi import SkyengApi
import allure


api=SkyengApi("https://api-teachers.skyeng.ru/v2/schedule/")
old_color='#81888D'
new_color='#D478F1'
old_title="Старое название события"
new_title='Новое название события'

@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-1")
@allure.title("Тестирование просмотра событий api")
@allure.feature ("Тестирование просмотра событий api")
@allure.story ("Проверка просмотра событий api")
@allure.severity("blocker")
def test_events_api():
    resp_body=api.events_api()
    assert len(resp_body)>0


@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-2")
@allure.title("Тестирование добавления события api")
@allure.feature ("Тестирование добавления события api")
@allure.story ("Проверка добавления события api")
@allure.severity("blocker")
def test_createPersonal_api():
    with allure.step('Получить список событий до'):
        body=api.events_api()
        len_before=len(body['data']['events'])
    task=api.createPersonal_api(old_title, old_color)
    taskId=task['data']['payload']['id']
    with allure.step('Получить список событий после'):
        body=api.events_api()
        len_after=len(body['data']['events'])
    with allure.step('Почистить за собой'):
        api.removePersonal_api(taskId)
    with allure.step('Сравнить, что длина списка событий после добавления больше на 1 списка событий до'):
        assert len_after-len_before==1


@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-3")
@allure.title("Тестирование удаления события api")
@allure.feature ("Тестирование удаления события api")
@allure.story ("Проверка удаления события api")
@allure.severity("blocker")
def test_removePersonal_api():
    with allure.step('Получить список событий до'):
        body=api.events_api()
        len_before=len(body['data']['events'])
    with allure.step("Получить ID события"):
        task=api.createPersonal_api(old_title, old_color)
        taskId=task['data']['payload']['id']
    api.removePersonal_api(taskId)
    with allure.step('Получить список событий после'):
        body=api.events_api()
        len_after=len(body['data']['events'])
    with allure.step('Сравнить, что длина списка событий после равна списку событий до'):
        assert len_after==len_before


@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-4")
@allure.title("Тестирование редактирования названия события api")
@allure.feature ("Тестирование редактирования названия события api")
@allure.story ("Проверка редактирования названия события api")
@allure.severity("blocker")
def test_updatePersonal_title_api():
    with allure.step('Получить список событий до'):
        body=api.events_api()
        len_before=len(body['data']['events'])
    with allure.step("Получить ID события"):
        task=api.createPersonal_api(old_title, old_color)
        taskId=task['data']['payload']['id']
    new_taskTitle=api.updatePersonal_title_api(taskId, new_title)
    with allure.step('Получить список событий после'):
        body=api.events_api()
        len_after=len(body['data']['events'])
    with allure.step('Почистить за собой'):
        api.removePersonal_api(taskId)
    with allure.step('Сравнить, что длина списка событий после добавления и редактирования события больше списка событий до на 1'):
        assert len_after-len_before==1
    with allure.step(f'Новое название события с ID {taskId} равно {new_title}'):
        assert new_taskTitle['data']['payload']['payload']['title']==new_title


@allure.epic("Skyeng API")
@allure.id("Scaeng Расписание api-5")
@allure.title("Тестирование редактирования цвета события по ID события api")
@allure.feature ("Тестирование редактирования цвета события по ID api")
@allure.story ("Проверка редактирования цвета события по ID api")
@allure.severity("blocker")
def test_updatePersonal_color_api():
    with allure.step('Получить список событий до'):
        body=api.events_api()
        len_before=len(body['data']['events'])    
    task=api.createPersonal_api(old_title, old_color)
    with allure.step('Получить ID'):
        taskId=task['data']['payload']['id']
    new_taskColor=api.updatePersonal_color_api(taskId, new_color)    
    with allure.step('Получить список событий после'):
        body=api.events_api()
        len_after=len(body['data']['events'])
    with allure.step('Почистить за собой'):
        api.removePersonal_api(taskId)
    with allure.step('Сравнить, что длина списка событий после добавления больше на 1 списка событий до'):
        assert len_after-len_before==1
    with allure.step(f'Новый цвет события {taskId} равен {new_color}'):
        assert new_taskColor['data']['payload']['payload']['color']==new_color