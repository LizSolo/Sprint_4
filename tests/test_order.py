import allure
from selenium import webdriver
from pages.order_page import OrderPage
from config import Config


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Процесс оформления заказа")
    @allure.description(
        "Этот тест проверяет весь процесс оформления заказа самоката, включая ввод данных, выбор опций и подтверждение заказа.")
    def test_order_process(self):
        self.driver.get(Config.ORDER_URL)
        order_page = OrderPage(self.driver)

        # Шаги для заказа самоката
        order_page.wait_for_load_order_page()
        order_page.enter_name(Config.NAME)
        order_page.enter_surname(Config.SURNAME)
        order_page.enter_address(Config.ADDRESS)
        order_page.select_metro_station(Config.METRO_STATION)
        order_page.enter_phone(Config.PHONE)
        order_page.click_next_button()
        order_page.set_delivery_date(Config.DELIVERY_DATE)
        order_page.select_lease_term(Config.LEASE_TERM)
        order_page.select_scooter_color()
        order_page.click_order_button()
        order_page.is_order_pop_up_visible()
        order_page.confirm_order()

    # Проверка видимости поп-апа подтверждения заказа
        assert order_page.is_order_confirm_pop_up_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
