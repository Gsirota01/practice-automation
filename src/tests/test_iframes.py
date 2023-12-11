import allure
import pytest

from pages.iframes_page import iframesPage

@allure.suite("Iframes")
@allure.description("The user navigates to the Iframes section and verifies the both iframes")
@allure.link("https://practice-automation.com/iframes","Website")
@allure.title("Verify the first iframe and his content")
@pytest.mark.iframe
@pytest.mark.parametrize("set_up_section", ["Iframes"], indirect=True)
def test_nat_geo_iframe(set_up_section):
    page = set_up_section

    iframes_page = iframesPage(page)
    iframes_page.validate_frame_text("I’m an iframe")
    iframes_page.validate_nat_geo_iframe_title()
    iframes_page.validate_nat_geo_menu()


@allure.suite("Iframes")
@allure.link("https://practice-automation.com/iframes","Website")
@allure.title("Verify the second iframe and his content")
@pytest.mark.iframe
@pytest.mark.parametrize("set_up_section", ["Iframes"], indirect=True)
def test_selenium_iframe(set_up_section):
    page = set_up_section

    iframes_page = iframesPage(page)
    iframes_page.validate_frame_text("Me too!")
    iframes_page.validate_selenium_logo()
