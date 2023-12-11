import allure
from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://practice-automation.com/")

    @allure.step("Navigate to {1} section")
    def navigate_to_section(self,text):
        self.page.click("text="+text)

    @allure.step("Validate title {1}")
    def validate_title(self,title):
        expect(self.page).to_have_title(title)
    

