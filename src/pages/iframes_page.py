import allure
from playwright.sync_api import expect

class iframesPage:
    def __init__(self, page):
        self.page = page
        self.nat_geo_frame = page.frame_locator("#frame2")
        self.nat_geo_menu = self.nat_geo_frame.get_by_label("Menu")
        self.selenium_frame = page.frame_locator("#frame1")
        self.selenium_logo = self.selenium_frame.get_by_role("link", name="Selenium logo green")
        self.nat_geo_frame_logo = self.nat_geo_frame.get_by_title("National Geographic", exact=True)
        self.frame_text = page.locator("#post-1129")

    @allure.step("Validate the menu category '{1}' appear")
    def validate_nat_geo_category(self,text):
        expect(self.nat_geo_frame.locator("#fittPortal_0").get_by_role("link", name=text)).to_be_visible()

    @allure.step("Validate the text '{1}' appear")
    def validate_frame_text(self,text):
        expect(self.frame_text).to_contain_text(text)

    @allure.step("Validate the title 'National Geographic' in the first iframe")
    def validate_nat_geo_iframe_title(self):
          expect(self.nat_geo_frame_logo).to_be_visible()

    @allure.step("Validate the categories in the menu")
    def validate_nat_geo_menu(self):
        self.nat_geo_menu.click()
        self.validate_nat_geo_category("Animals")
        self.validate_nat_geo_category("Environment")
        self.validate_nat_geo_category("History & Culture")
        self.validate_nat_geo_category("Science")


    @allure.step("Validate the title 'Selenium' in the second iframe")
    def validate_selenium_logo(self):
          expect(self.selenium_logo).to_be_visible()




