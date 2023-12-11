import time
import allure
from playwright.sync_api import expect


class JavascriptDelaysPage:
    def __init__(self, page):
        self.page = page

        self.start_button = page.locator("button#start")
        self.delay_input = page.locator("input#delay")

    @allure.step("Click start button")  
    def click_start_button(self):
        self.start_button.click()

    @allure.step("Wait delay page")
    def wait_delay_page(self):
        time.sleep(10)
    
    @allure.step("Verify if the text 'Liftoff!' is present")
    def validate_delay_input(self):
        expect(self.delay_input).to_have_value('Liftoff!')