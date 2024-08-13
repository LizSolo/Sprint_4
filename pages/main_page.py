from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_header_order_button(self):
        self.driver.find_element(*Locators.HEADER_ORDER_BUTTON).click()

    def click_order_button(self):
        self.scroll_to_element(Locators.HOME_ORDER_BUTTON)
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.HOME_ORDER_BUTTON)
        ).click()

    def click_logo_yandex(self):
        self.driver.find_element(*Locators.LOGO_YANDEX).click()

    def click_button(self, button_id):
        self.scroll_to_element((By.ID, button_id))
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, button_id))
        ).click()

    def is_panel_visible(self, panel_id):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, panel_id)))

    def get_answer_text(self, panel_id):
        return WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located((By.ID, panel_id))
        ).text
