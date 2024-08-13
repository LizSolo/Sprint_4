import pytest
import allure
from selenium import webdriver
from config import Config
from pages.main_page import MainPage


class TestFaq:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("button_id, panel_id, expected_text", [
        (Config.BUTTON_ID_0, Config.PANEL_ID_0, Config.EXPECTED_TEXT_0),
        (Config.BUTTON_ID_1, Config.PANEL_ID_1, Config.EXPECTED_TEXT_1),
        (Config.BUTTON_ID_2, Config.PANEL_ID_2, Config.EXPECTED_TEXT_2),
        (Config.BUTTON_ID_3, Config.PANEL_ID_3, Config.EXPECTED_TEXT_3),
        (Config.BUTTON_ID_4, Config.PANEL_ID_4, Config.EXPECTED_TEXT_4),
        (Config.BUTTON_ID_5, Config.PANEL_ID_5, Config.EXPECTED_TEXT_5),
        (Config.BUTTON_ID_6, Config.PANEL_ID_6, Config.EXPECTED_TEXT_6),
        (Config.BUTTON_ID_7, Config.PANEL_ID_7, Config.EXPECTED_TEXT_7),
    ])
    @allure.title("Проверка 'Вопросы о важном'")
    @allure.description("Этот тест проверяет отображение текстов ответов для кнопок в разделе важных вопросов.")
    @allure.step("Получаем текст ответа и сравниваем с ожидаемым текстом.")
    def test_important_questions(self, button_id, panel_id, expected_text):
        self.driver.get(Config.BASE_URL)
        main_page = MainPage(self.driver)
        main_page.click_button(button_id)
        assert main_page.is_panel_visible(panel_id)
        text_answer = main_page.get_answer_text(panel_id)
        assert text_answer == expected_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
