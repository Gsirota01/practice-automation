from playwright.sync_api import expect
import allure

class PopupsPage:
    def __init__(self, page):
        self.page = page
        self.confirm_popup_text = page.locator("#confirmResult")
        self.prompt_popup_text = page.locator("#promptResult")
        self.tooltip = page.get_by_text("<< click me to see a tooltip")
        self.tooltip_text = page.locator("#myTooltip")
    
    def validate_alert(self, dialog, action):
        if action == "dismiss":
            dialog.dismiss()
        if dialog.type == "alert" and action == "accept" :
            assert dialog.message == "Hi there, pal!"
            dialog.dismiss()
        if dialog.type == "prompt" and action == "accept":
            assert dialog.message == "Hi there, what's your name?"
            dialog.accept("Name")
        if dialog.type == "confirm" and action == "accept":
            assert dialog.message == "OK or Cancel, which will it be?"
            dialog.accept()

    @allure.step("Click on {1} button")
    def click_popup(self,text,action):
        self.add_event_listener(action)
        self.page.get_by_role("button", name=text).click()

    def add_event_listener(self, action):
        self.page.once("dialog", lambda dialog: self.validate_alert(dialog,action))

    @allure.step("Validate that text 'OK it is!' appear in the confirm")
    def validate_accept_confirm_popup(self):
        expect(self.confirm_popup_text).to_contain_text("OK it is!")

    @allure.step("Validate that text 'Cancel, it is!' appear in the confirm")
    def validate_dismiss_confirm_popup(self):
        expect(self.confirm_popup_text).to_contain_text("Cancel it is!")
    
    @allure.step("Validate that the text 'Fine, be that way...!' appear")
    def validate_prompt_popup_without_text(self):
        expect(self.prompt_popup_text).to_contain_text('Fine, be that way...')
    
    @allure.step("Validate that the text Nice to meet you,{1}! appear")
    def validate_prompt_popup(self,text):
        expect(self.prompt_popup_text).to_contain_text(f'Nice to meet you, {text}!')
        
    @allure.step("Validate tooltip appear and validate text")
    def click_tooltip(self):
        self.tooltip.click()
    
    @allure.step("Validate that text 'Cool text' appear in the tooltip")
    def validate_tooltip_text(self):
        expect(self.tooltip_text).to_contain_text("Cool text")