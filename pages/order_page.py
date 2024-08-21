from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import  allure


class OrderPage(BasePage):

    @allure.step('Заполняем поле Имя')
    def input_name(self, name):
        self.wait_and_find_element(OrderPageLocators.INPUT_NAME).send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def input_surname(self, surname):
        self.wait_and_find_element(OrderPageLocators.INPUT_SURNAME).send_keys(surname)

    @allure.step('Заполняем поле Адрес')
    def input_address(self, address):
        self.wait_and_find_element(OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self, station):
        metro_input = self.wait_and_find_element(OrderPageLocators.INPUT_METRO_STATION)
        metro_input.send_keys(station)
        self.wait_and_clickable(OrderPageLocators.METRO_STATION_OPTION(station)).click()

    @allure.step('Заполняем поле Телефон')
    def input_phone(self, phone):
        self.wait_and_find_element(OrderPageLocators.INPUT_PHONE).send_keys(phone)

    @allure.step('Нажимаем на кнопку Далее')
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем дату доставки')
    def set_delivery_date(self, date):
        self.wait_and_clickable(OrderPageLocators.DELIVERY_DATE_INPUT).click()
        self.wait_and_find_element(OrderPageLocators.DELIVERY_DATE_INPUT).send_keys(date)
        self.click_element(OrderPageLocators.BODY)

    @allure.step('Заполняем срок аренды')
    def select_lease_term(self, term):
        self.click_element(OrderPageLocators.LEASE_TERM)
        self.wait_and_clickable(OrderPageLocators.TERM_OPTION(term)).click()

    @allure.step('Выбираем цвет самоката')
    def select_scooter_color(self):
        self.click_element(OrderPageLocators.SCOOTER_COLOR)

    @allure.step('Нажимаем на кнопку Заказать')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Нажимаем на кнопку Да')
    def confirm_order(self):
        self.wait_and_clickable(OrderPageLocators.BUTTON_YES).click()

    @allure.step('Получаем текст подтверждения заказа')
    def get_order_confirmation_text(self):
        element = self.wait_and_find_element(OrderPageLocators.ORDER_CONFIRM_POP_UP)
        return element.text

    @allure.step('Нажимаем на логотип Самокат')
    def click_logo_scooter(self):
        self.click_element(OrderPageLocators.LOGO_SCOOTER)
