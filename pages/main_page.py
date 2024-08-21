from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    @allure.step('Нажимаем на кнопку Заказать в хедере')
    def click_header_order_button(self):
         self.click_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Нажимаем на вопрос')
    def click_button(self, button_id):
        self.wait_and_click(By.ID, button_id)

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text(self, panel_id):
        return self.get_text_from_element(By.ID, panel_id)

    @allure.step('Нажимаем на логотип Яндекс')
    def click_logo_yandex(self):
        self.click_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Нажимаем на кнопку Заказать')
    def click_order_button(self):
        self.scroll_and_click(MainPageLocators.HOME_ORDER_BUTTON)

