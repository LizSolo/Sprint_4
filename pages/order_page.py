from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import Config
from locators import Locators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 5).until(ec.url_to_be(Config.ORDER_URL))

    def enter_name(self, name):
        self.driver.find_element(*Locators.INPUT_NAME).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element(*Locators.INPUT_SURNAME).send_keys(surname)

    def enter_address(self, address):
        self.driver.find_element(*Locators.INPUT_ADDRESS).send_keys(address)

    def select_metro_station(self, station):
        metro_input = self.driver.find_element(*Locators.INPUT_METRO_STATION)
        metro_input.send_keys(station)
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, f"//div[text()='{station}']"))
        ).click()

    def enter_phone(self, phone):
        self.driver.find_element(*Locators.INPUT_PHONE).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*Locators.NEXT_BUTTON).click()

    def click_logo_scooter(self):
        self.driver.find_element(*Locators.LOGO_SCOOTER).click()

    def set_delivery_date(self, date):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.DELIVERY_DATE_INPUT)
        ).click()
        self.driver.find_element(*Locators.DELIVERY_DATE_INPUT).send_keys(date)
        #  Закрыть дата пикер
        self.driver.find_element(By.XPATH, "//body").click()

    def select_lease_term(self, term):
        lease_dropdown = self.driver.find_element(*Locators.LEASE_TERM)
        lease_dropdown.click()
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, f"//div[text()='{term}']"))
        ).click()

    def select_scooter_color(self):
        self.driver.find_element(*Locators.SCOOTER_COLOR).click()

    def click_order_button(self):
        self.driver.find_element(*Locators.ORDER_BUTTON).click()

    def is_order_pop_up_visible(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_POP_UP)
        )

    def confirm_order(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.BUTTON_YES)
        ).click()

    def is_order_confirm_pop_up_visible(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_CONFIRM_POP_UP)
        )
