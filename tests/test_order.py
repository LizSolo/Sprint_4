import allure
import data
from conftest import driver
from pages.order_page import OrderPage


class TestOrder:

    @allure.title("Процесс оформления заказа")
    @allure.description(
        "Этот тест проверяет весь процесс оформления заказа самоката, включая ввод данных, выбор опций и подтверждение заказа.")
    def test_confirm_order(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(data.Urls.SCOOTER_ORDER)
        order_page.input_name(data.Order.NAME)
        order_page.input_surname(data.Order.SURNAME)
        order_page.input_address(data.Order.ADDRESS)
        order_page.select_metro_station(data.Order.METRO_STATION)
        order_page.input_phone(data.Order.PHONE)
        order_page.click_next_button()
        order_page.set_delivery_date(data.Order.DELIVERY_DATE)
        order_page.select_lease_term(data.Order.LEASE_TERM)
        order_page.select_scooter_color()
        order_page.click_order_button()
        order_page.confirm_order()
        confirmation_text = order_page.get_order_confirmation_text()

        # Сравнение текста с ожидаемым значением
        assert data.Order.ORDER_CONFIRM_TEXT in confirmation_text
