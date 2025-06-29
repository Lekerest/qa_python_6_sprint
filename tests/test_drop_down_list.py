import pytest
from locators.locators_drop_down_list import LocatorsDropDownList
from pages.base_page import BasePage
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
    def test_drop_down_list(self, driver, locator_question, locator_answer, question):
        general = BasePage(driver)
        methods_drop_down_list = PageDropDownList(driver)
        general.click_on_button_cookie_accept()
        methods_drop_down_list.scroll_to_element(locator_question)
        methods_drop_down_list.click_on_the_question(locator_question)

        question_text = methods_drop_down_list.get_text_faq(locator_question)
        answer_text = methods_drop_down_list.get_text_faq(locator_answer)

        assert question_text == question, f"Текст вопроса не совпадает не соответствует ожидаемому"
        assert answer_text == FAQDropDownList.FaqList[question_text], "Ответ не соответствует тексту вопроса"
