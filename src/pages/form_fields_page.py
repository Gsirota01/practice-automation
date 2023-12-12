from playwright.sync_api import expect
import allure
class FormFieldsPage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.get_by_label("Name(required)")
        self.water_checkbox = page.get_by_label("Water")
        self.wine_checkbox = page.get_by_label("Wine")
        self.red_radio_button = page.get_by_label("Red", exact=True)
        self.have_siblings = page.locator("#g1103-doyouhaveanysiblings")
        self.have_siblings_options = page.get_by_label("Do you have any siblings?")
        self.fast_animals_form = page.get_by_role("form")
        self.fast_animals_list = page.get_by_role("list")
        self.email_input = page.get_by_role("textbox", name="Email")
        self.message_input = page.locator("#contact-form-comment-message")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.form_success = page.locator(".contact-form-submission")
        self.back_button = page.get_by_role("link", name="Go back")

    @allure.step("Complete the form")
    def complete_form(self):
        self.complete_name()
        self.select_favorite_drinks()
        self.select_favorite_color()
        self.complete_have_siblings()
        self.complete_email()
        self.complete_message()

    @allure.step("Complete name")
    def complete_name(self):
        self.name_input.fill("Name")

    @allure.step("Select favorite drinks")
    def select_favorite_drinks(self):
        self.water_checkbox.check()
        self.wine_checkbox.check()
    
    @allure.step("Select favorite color")
    def select_favorite_color(self):
        self.red_radio_button.check()

    @allure.step("Complete have siblings")
    def complete_have_siblings(self):
        self.have_siblings.click()
        self.have_siblings_options.select_option("No")    
    
    @allure.step("Validate animals list")
    def validate_animals_list(self):
        expect(self.fast_animals_form).to_contain_text("Fast animals")
        expect(self.fast_animals_list).to_contain_text("Falcon")
        expect(self.fast_animals_list).to_contain_text("Eagle")
        expect(self.fast_animals_list).to_contain_text("Horsefly")
        expect(self.fast_animals_list).to_contain_text("Cheetah")
    
    @allure.step("Complete email")
    def complete_email(self):
        self.email_input.fill("mailprueba@mail.com")

    @allure.step("Complete message")
    def complete_message(self):
        self.message_input.fill("Message")
    
    @allure.step("Submit form")
    def submit_form(self):
        self.submit_button.click()
    
    @allure.step("Validate send form")
    def validate_send_form(self):
        expect(self.form_success).to_contain_text("Your message has been sent")
        expect(self.form_success).to_contain_text("Name")
        expect(self.form_success).to_contain_text("Water")
        expect(self.form_success).to_contain_text("Wine")
        expect(self.form_success).to_contain_text("Red")
        expect(self.form_success).to_contain_text("No")
        expect(self.form_success).to_contain_text("mailprueba@mail.com")
        expect(self.form_success).to_contain_text("Message")


    @allure.step("Go back")
    def go_back(self):
        self.back_button.click()
    
    
    @allure.step("Validate title {1}")
    def validate_title(self,title):
        expect(self.page).to_have_title(title)
    