import pytest
from locators.locators_drop_down_list import LocatorsDropDownList
from pages.base_page import BasePage
from pages.page_drop_down_list import PageDropDownList



class TestDropDownList:

    @pytest.mark.parametrize(
    "locator",
        [
            LocatorsDropDownList.FIRST_QUESTION,
            LocatorsDropDownList.SECOND_QUESTION,
            LocatorsDropDownList.THIRD_QUESTION,
            LocatorsDropDownList.FOURTH_QUESTION,
            LocatorsDropDownList.FIFTH_QUESTION,
            LocatorsDropDownList.SIXTH_QUESTION,
            LocatorsDropDownList.SEVENTH_QUESTION,
            LocatorsDropDownList.EIGHTH_QUESTION
        ]
    )
    def test_drop_down_list(self, driver, locator):
        general = BasePage(driver)
        methods_drop_down_list = PageDropDownList(driver)
        general.click_on_button_cookie_accept()
        methods_drop_down_list.scroll_to_element(locator)
        methods_drop_down_list.click_on_the_question(locator)
        assert methods_drop_down_list.get_text_question(locator) ==
