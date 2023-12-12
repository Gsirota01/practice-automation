import pytest
import allure
from playwright.sync_api import sync_playwright,Playwright

from pages.home_page import HomePage

@pytest.fixture(scope="package")
@allure.title("Setup Browser")
def set_up(playwright : Playwright)-> None:
    browser = playwright.chromium.launch(headless=True)
    browser_context = browser.new_context(record_video_dir="reports/videos/")
    browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page =  browser_context.new_page()
    yield page

    browser_context.tracing.stop(path = "logs/trace.zip")
    browser_context.close()

@pytest.fixture(scope="package")
@allure.title("Setup Browser and navigate to {section_name} section")
def set_up_section(playwright : Playwright, request)-> None:
    section_name = request.param
    allure.dynamic.title("Setup Browser and navigate to {} section".format(section_name))
    
    browser = playwright.chromium.launch(headless=True)
    browser_context = browser.new_context(record_video_dir="reports/videos/")
    browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page =  browser_context.new_page()

    home_page = HomePage(page)

    home_page.navigate()
    home_page.navigate_to_section(section_name)
    home_page.validate_title(f'{section_name} | automateNow | Practice')

    yield page

    browser_context.tracing.stop(path = "logs/trace.zip")
    browser_context.close()
