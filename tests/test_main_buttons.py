import data
import allure
from pages.main_page import MainPage
from conftest import driver
from pages.order_page import OrderPage


class TestMainButtons:

    @allure.title("Проверка кнопки заказа в хедере")
    @allure.description(
        "Этот тест проверяет, что кнопка заказа в хедере работает корректно и загружает страницу заказа.")
    def test_header_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.SCOOTER)
        main_page.click_header_order_button()
        assert driver.current_url == data.Urls.SCOOTER_ORDER

    @allure.title("Проверка логотипа Яндекс")
    @allure.description(
        "Этот тест проверяет, что клик по логотипу Яндекс на главной странице открывает страницу Яндекс.Дзен.")
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.SCOOTER)
        main_page.click_logo_yandex()
        main_page.switch_to_new_tab_and_wait_for_url(data.Urls.DZEN_URL)
        assert driver.current_url == data.Urls.DZEN_URL

    @allure.title("Проверка логотипа скутера")
    @allure.description(
        "Этот тест проверяет, что клик по логотипу скутера на странице заказа возвращает на главную страницу.")
    def test_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(data.Urls.SCOOTER_ORDER)
        order_page.click_logo_scooter()
        assert driver.current_url == data.Urls.SCOOTER

    @allure.title("Проверка кнопки заказа на главной странице")
    @allure.description(
        "Этот тест проверяет, что кнопка заказа на главной странице работает корректно и загружает страницу заказа.")
    def test_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.SCOOTER)
        main_page.click_order_button()
        assert driver.current_url == data.Urls.SCOOTER_ORDER
