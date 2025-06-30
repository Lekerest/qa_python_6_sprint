import pytest
import allure
from locators.locators_drop_down_list import LocatorsDropDownList
from pages.page_drop_down_list import PageDropDownList
from helpers import FAQDropDownList


class TestDropDownList:

    @pytest.mark.parametrize(
        "locator_question, locator_answer, question",
        [
            (LocatorsDropDownList.FIRST_QUESTION, LocatorsDropDownList.FIRST_ANSWER, FAQDropDownList.FIRST_QUESTION),
            (LocatorsDropDownList.SECOND_QUESTION, LocatorsDropDownList.SECOND_ANSWER, FAQDropDownList.SECOND_QUESTION),
            (LocatorsDropDownList.THIRD_QUESTION, LocatorsDropDownList.THIRD_ANSWER, FAQDropDownList.THIRD_QUESTION),
            (LocatorsDropDownList.FOURTH_QUESTION, LocatorsDropDownList.FOURTH_ANSWER, FAQDropDownList.FOURTH_QUESTION),
            (LocatorsDropDownList.FIFTH_QUESTION, LocatorsDropDownList.FIFTH_ANSWER, FAQDropDownList.FIFTH_QUESTION),
            (LocatorsDropDownList.SIXTH_QUESTION, LocatorsDropDownList.SIXTH_ANSWER, FAQDropDownList.SIXTH_QUESTION),
            (LocatorsDropDownList.SEVENTH_QUESTION, LocatorsDropDownList.SEVENTH_ANSWER, FAQDropDownList.SEVENTH_QUESTION),
            (LocatorsDropDownList.EIGHTH_QUESTION, LocatorsDropDownList.EIGHTH_ANSWER, FAQDropDownList.EIGHTH_QUESTION),
        ]
    )
    @allure.title("Проверка вопроса FAQ: {question}")
    @allure.step("Тестируем раскрытие вопроса: '{question}'")
    def test_drop_down_list(self, driver, locator_question, locator_answer, question):
        methods_drop_down_list = PageDropDownList(driver)

        methods_drop_down_list.scroll_to_element(locator_question)

        methods_drop_down_list.click_on_the_question(locator_question)

        with allure.step("Получение текста вопроса и ответа"):
            question_text = methods_drop_down_list.get_text_faq(locator_question)
            answer_text = methods_drop_down_list.get_text_faq(locator_answer)

        with allure.step("Проверка текста вопроса"):
            assert question_text == question, "Текст вопроса не совпадает с ожидаемым"

        with allure.step("Проверка соответствия ответа вопросу"):
            expected_answer = FAQDropDownList.FaqList.get(question_text)
            assert answer_text == expected_answer, "Ответ не соответствует тексту вопроса"