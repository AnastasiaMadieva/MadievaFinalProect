from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__url = "https://www.aviasales.ru/"

    @allure.step("Перейти на страницу aviasales")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        self.__driver.implicitly_wait(15)
        curl = self.__driver.current_url
        return curl

    @allure.step('Ввести аэропорт вылета')
    def input_from_origin(self, from_aer):
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-test-id="accept-cookies-button"]').click()
        self.__driver.find_element(
            By.CSS_SELECTOR, '#avia_form_origin-input').clear()
        self.__driver.find_element(
            By.CSS_SELECTOR, '#avia_form_origin-input').send_keys(from_aer)
        self.__driver.find_element(
            By.CSS_SELECTOR, '#avia_form_origin-input').is_displayed()
        value = self.__driver.find_element(
            By.CSS_SELECTOR, '#avia_form_origin-input').get_attribute('value')
        self.__driver.find_element(
            By.CSS_SELECTOR, '#avia_form_destination-input').clear()
        return value

    @allure.step('Ввести аэропорт прибытия')
    def input_from_destination(self, to_aer):
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-test-id="accept-cookies-button"]').click()
        self.__driver.find_element(
            By.CSS_SELECTOR, '#avia_form_destination-input').clear()
        self.__driver.find_element(
            By.CSS_SELECTOR, '#avia_form_destination-input').send_keys(to_aer)
        self.__driver.find_element(
            By.CSS_SELECTOR, '#avia_form_destination-input').is_displayed()
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-test-id="start-date-field"]').click()
        value = self.__driver.find_element(
            By.CSS_SELECTOR, '#avia_form_destination-input').get_attribute('value')
        return value

    @allure.step('Выбрать дату')
    def start_date(self, data):
        with allure.step('Принять cookie'):
            self.__driver.find_element(
                By.CSS_SELECTOR, '[data-test-id="accept-cookies-button"]').click()
        with allure.step('Нажать на поле когда'):
            self.__driver.find_element(
                By.CSS_SELECTOR, '[data-test-id="start-date-field"]').click()
        with allure.step(f'Нажать на дату {data}'):
            self.__driver.find_element(
                By.CSS_SELECTOR, f'[data-test-id="date-{data}"]').click()
        with allure.step('Нажать на Кнопку Обратный билет не нужен'):
            self.__driver.find_element(
                By.CSS_SELECTOR, '[data-test-id="calendar-action-button"]').click()
        with allure.step('Ждем отображения выбранной даты в поле когда'):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test-id="start-date-value"]')))

    @allure.step('Поиск билета')
    def submit_clic(self, data, from_aer, to_aer):
        with allure.step('Принять cookie'):
            self.__driver.find_element(
                By.CSS_SELECTOR, '[data-test-id="accept-cookies-button"]').click()
        with allure.step('Ввести аэропорт вылета'):
            self.__driver.find_element(
                By.CSS_SELECTOR, '#avia_form_origin-input').clear()
            self.__driver.find_element(
                By.CSS_SELECTOR, '#avia_form_origin-input').send_keys(from_aer)
            self.__driver.find_element(
                By.CSS_SELECTOR, '#avia_form_origin-input').is_displayed()
            self.__driver.implicitly_wait(2)
        with allure.step('Ввести аэропорт прибытия'):
            self.__driver.find_element(
                By.CSS_SELECTOR, '#avia_form_destination-input').clear()
            self.__driver.find_element(
                By.CSS_SELECTOR, '#avia_form_destination-input').send_keys(to_aer)
            self.__driver.find_element(
                By.CSS_SELECTOR, '#avia_form_origin-input').is_displayed()
            self.__driver.implicitly_wait(2)
        with allure.step('Нажать на поле когда'):
            self.__driver.find_element(
                By.CSS_SELECTOR, '[data-test-id="start-date-field"]').click()
        with allure.step(f'Нажать на дату {data}'):
            self.__driver.find_element(
                By.CSS_SELECTOR, f'[data-test-id="date-{data}"]').click()
        with allure.step('Нажать на Кнопку Обратный билет не нужен'):
            self.__driver.find_element(
                By.CSS_SELECTOR, '[data-test-id="calendar-action-button"]').click()
        with allure.step('Нажать на Кнопку Найти билеты'):
            self.__driver.find_element(
                By.CSS_SELECTOR, '[data-test-id="form-submit"]').click()
        with allure.step('Ждем прогрузки всех рейсов'):
            WebDriverWait(self.__driver, 120).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.app__container')))
