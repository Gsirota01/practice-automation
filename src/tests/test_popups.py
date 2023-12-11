import allure
import pytest

from pages.popups_page import PopupsPage

@allure.suite("Popups")
@allure.description("The user navigates to the Popups section and verifies the differents popups")
@allure.label("owner","Gabriel Sirota")
@allure.link("https://practice-automation.com/","Website")

@allure.title("Accept alert popup")
@pytest.mark.popup
@pytest.mark.parametrize("set_up_section", ["Popups"], indirect=True)
def test_accept_alert_popup(set_up_section):
    page = set_up_section

    popups_page_accept = PopupsPage(page)
    popups_page_accept.click_popup("Alert Popup","accept")

@allure.suite("Popups")
@allure.title("Dismiss confirm popup")
@pytest.mark.popup
@pytest.mark.parametrize("set_up_section", ["Popups"], indirect=True)
def test_dismiss_confirm_popup(set_up_section):
    page = set_up_section

    popups_page = PopupsPage(page)

    popups_page.click_popup("Confirm Popup", "dismiss")
    popups_page.validate_dismiss_confirm_popup()

@allure.suite("Popups")
@allure.title("Accept confirm popup")
@pytest.mark.popup
@pytest.mark.parametrize("set_up_section", ["Popups"], indirect=True)
def test_accept_confirm_popup(set_up_section):
    page = set_up_section

    popups_page = PopupsPage(page)

    popups_page.click_popup("Confirm Popup", "accept")
    popups_page.validate_accept_confirm_popup()

@allure.suite("Popups")
@allure.title("Dismiss prompt popup")
@pytest.mark.popup
@pytest.mark.parametrize("set_up_section", ["Popups"], indirect=True)
def test_prompt_popup_without_text(set_up_section):
    page = set_up_section
    popups_page_dismiss = PopupsPage(page)

    popups_page_dismiss.click_popup("Prompt Popup","dismiss")
    popups_page_dismiss.validate_prompt_popup_without_text()

@allure.suite("Popups")
@allure.title("Complete and accept prompt popup")
@pytest.mark.popup
@pytest.mark.parametrize("set_up_section", ["Popups"], indirect=True)
def test_prompt_popup_with_text(set_up_section):
    page = set_up_section
    popups_page_dismiss = PopupsPage(page)

    popups_page_dismiss.click_popup("Prompt Popup","accept")
    popups_page_dismiss.validate_prompt_popup("Name")

@allure.suite("Popups")
@allure.title("Verify tooltip")
@pytest.mark.popup
@pytest.mark.parametrize("set_up_section", ["Popups"], indirect=True)
def test_tooltip_appear(set_up_section):
    page = set_up_section
    popups_page_dismiss = PopupsPage(page)

    popups_page_dismiss.click_tooltip()
    popups_page_dismiss.validate_tooltip_text()

