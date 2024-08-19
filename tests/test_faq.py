import allure
import pytest
import data
from conftest import driver
from pages.main_page import MainPage


class TestFaq:

    @pytest.mark.parametrize("button_id, panel_id, expected_text", [
        (data.Faq.BUTTON_ID_0, data.Faq.PANEL_ID_0, data.Faq.EXPECTED_TEXT_0),
        (data.Faq.BUTTON_ID_1, data.Faq.PANEL_ID_1, data.Faq.EXPECTED_TEXT_1),
        (data.Faq.BUTTON_ID_2, data.Faq.PANEL_ID_2, data.Faq.EXPECTED_TEXT_2),
        (data.Faq.BUTTON_ID_3, data.Faq.PANEL_ID_3, data.Faq.EXPECTED_TEXT_3),
        (data.Faq.BUTTON_ID_4, data.Faq.PANEL_ID_4, data.Faq.EXPECTED_TEXT_4),
        (data.Faq.BUTTON_ID_5, data.Faq.PANEL_ID_5, data.Faq.EXPECTED_TEXT_5),
        (data.Faq.BUTTON_ID_6, data.Faq.PANEL_ID_6, data.Faq.EXPECTED_TEXT_6),
        (data.Faq.BUTTON_ID_7, data.Faq.PANEL_ID_7, data.Faq.EXPECTED_TEXT_7),
    ])

    @allure.title("Проверка 'Вопросы о важном'")
    @allure.description("Этот тест проверяет отображение текстов ответов для кнопок в разделе важных вопросов.")
    def test_important_questions(self, driver, button_id, panel_id, expected_text):
        main_page = MainPage(driver)
        main_page.open_page(data.Urls.SCOOTER)
        main_page.click_button(button_id)
        text_answer = main_page.get_answer_text(panel_id)
        assert text_answer == expected_text