from selenium import webdriver
from pages.authPage import AuthPage
from pages.mainPage import MainPage
import allure


from_aer = "Казань"
to_aer = "Москва"
start_date = "08.04.2025"


@allure.epic("AVIASELS UI")
@allure.id("aviaseils_ui-1")
@allure.title("Тестирование авторизации ui")
@allure.story("Проверка авторизации ui")
@allure.severity("blocker")
def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.open_menu()
    auth_page.click_btn_enter()
    auth_page.click_btn_VK()
    current_url = auth_page.get_current_url()
    assert current_url == "https://www.aviasales.ru/?params=UFA1"


@allure.epic("AVIASELS UI")
@allure.id("aviaseils_ui-2")
@allure.title("Тестирование поля откуда ui")
@allure.feature("Тестирование поля откуда ui")
@allure.story("Проверка поля откуда ui")
@allure.severity("blocker")
def test_input_from(browser):
    main_page = MainPage(browser)
    main_page.go()
    value_from = main_page.input_from_origin(from_aer)
    curient_url = main_page.get_current_url()
    assert curient_url == "https://www.aviasales.ru/?params=KZN1"
    assert value_from == from_aer


@allure.epic("AVIASELS UI")
@allure.id("aviaseils_ui-3")
@allure.title("Тестирование поля куда ui")
@allure.feature("Тестирование поля куда ui")
@allure.story("Проверка поля куда ui")
def test_input_destination(browser):
    main_page = MainPage(browser)
    main_page.go()
    value_to = main_page.input_from_destination(to_aer)
    curient_url = main_page.get_current_url()
    assert curient_url == "https://www.aviasales.ru/?params=UFAMOW1"
    assert value_to == to_aer


@allure.epic("AVIASELS UI")
@allure.id("aviaseils_ui-4")
@allure.title("Тестирование поля дата ui")
@allure.feature("Тестирование поля дата ui")
@allure.story("Проверка поля дата ui")
@allure.severity("blocker")
def test_start_date(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.start_date(start_date)
    curient_url = main_page.get_current_url()
    assert curient_url == "https://www.aviasales.ru/?params=UFA08041"


@allure.epic("AVIASELS UI")
@allure.id("aviaseils_ui-5")
@allure.title("Тестирование поиска билета ui")
@allure.feature("Тестирование поиска билета ui")
@allure.story("Проверка поиска билета ui")
@allure.severity("blocker")
def test_submit_click(browser):
    main_page = MainPage(browser)
    main_page.go()
    value_start_date = main_page.submit_clic(start_date, from_aer, to_aer)
    curient_url = main_page.get_current_url()
    assert curient_url == "https://www.aviasales.ru/?params=UFA08041"
    assert value_start_date == start_date
