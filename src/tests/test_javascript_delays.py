import allure
import pytest

from pages.javascript_delays_page import JavascriptDelaysPage


@allure.suite("Test Javascript Delays")
@allure.description("The user navigates to the Javascript Delays section and verifies the delay")
@allure.link("https://practice-automation.com/javascript-delays","Website")
@pytest.mark.delays
@pytest.mark.parametrize("set_up_section", ["JavaScript Delays"], indirect=True)
def test_javascript_delays(set_up_section):
    page = set_up_section

    javascript_delays_page = JavascriptDelaysPage(page)

    javascript_delays_page.click_start_button()
    javascript_delays_page.wait_delay_page()
    javascript_delays_page.validate_delay_input()

