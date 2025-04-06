from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from tests.dataProvider import DataProvider



class AuthPage:
    
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.aviasales.ru/"
        self.__driver = driver
        self.__url_VK_ID = "https://id.vk.com/"

    @allure.step("Перейти на страницу авторизации")
    def go(self):
            self.__driver.get(self.__url)     

    @allure.step("Нажимаем на иконку с человечком в верхнем правом углу:")
    def open_menu(self):
            self.__driver.find_element(By.CSS_SELECTOR, '[data-test-id="profile-button"]').click()
           
    @allure.step("Нажимаем на кнопку Войти")   
    def click_btn_enter(self):
            self.__driver.find_element(By.CSS_SELECTOR, '[data-test-id="button"]').click() 

    @allure.step("Нажимаем на кнопку Войти с VK ID")   
    def click_btn_VK(self):
            self.__driver.find_element(By.CSS_SELECTOR, '.s__dqLrjmV81lbY2ctpQQWt.s__WErm7_CLb_ylgTog3lrX.s__OWNGeBF_djpi7qoBOxk4.s__f1UsosWbVEKg57lLhkEC.s__ceBrcQp1NVw3cf8D8Rmt.s__nW_dCpJNx3Us1pJt10Zm.s__JiaBa1eD25_ba_xHC8h9.s__fdTWBESWQ61NEnOZDp17').click() 

    @allure.step("Нажимаем на кнопку + в окне авторизации Вк")   
    def click_btn_add(self):
            self.__driver.get(self.__url_VK_ID)
            self.__driver.find_element(By.XPATH, '//span[text()="Войти"]').click()
           
    @allure.step("Авторизоваться под {phone}:{password}")
    def login_as(self, phone: str, password: str):
            self.__driver.get(self.__url_VK_ID)
            self.__driver.find_element(By.CSS_SELECTOR, 'div.vkuiSegmentedControl__slider').click()
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="+7 000 000 00 00"]')))
            self.__driver.find_element(By.CSS_SELECTOR, '.vkuiFormField__content').send_keys(phone)
            self.__driver.find_element(By.CSS_SELECTOR, 'button.vkuiButton').click()  

            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#otp")))            
            self.__driver.find_element(By.XPATH, '//span[text()="Войти при помощи пароля"]').click()

            self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
            self.__driver.find_element(By.XPATH, '//span[text()="Войти"]').click()

            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[.data-loading="false"]')))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
            return self.__driver.current_url
