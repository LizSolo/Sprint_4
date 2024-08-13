import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestMainButton:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Проверка кнопки заказа в хедере")
    @allure.description("Этот тест проверяет, что кнопка заказа в хедере работает корректно и загружает страницу заказа.")
    def test_header_order_button(self):
        self.driver.get(Config.BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_header_order_button()
        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()

    @allure.title("Проверка кнопки заказа на главной странице")
    @allure.description(
        "Этот тест проверяет, что кнопка заказа на главной странице работает корректно и загружает страницу заказа.")
    def test_order_button(self):
        self.driver.get(Config.BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_order_button()
        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()

    @allure.title("Проверка логотипа скутера")
    @allure.description(
        "Этот тест проверяет, что клик по логотипу скутера на странице заказа возвращает на главную страницу.")
    def test_logo_scooter(self):
        self.driver.get(Config.ORDER_URL)
        order_page = OrderPage(self.driver)
        order_page.click_logo_scooter()
        WebDriverWait(self.driver, 5).until(ec.url_to_be(Config.BASE_URL))

    @allure.title("Проверка логотипа Яндекс")
    @allure.description(
        "Этот тест проверяет, что клик по логотипу Яндекс на главной странице открывает страницу Яндекс.Дзен.")
    def test_logo_yandex(self):
        self.driver.get(Config.BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_logo_yandex()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        WebDriverWait(self.driver, 15).until(ec.url_to_be(Config.DZEN_URL))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
