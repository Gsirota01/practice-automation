import allure
import pytest

from pages.form_fields_page import FormFieldsPage

global browser_context,page

@allure.suite("Form Fields")
@allure.title("Test Form Fields")
@allure.description("The user navigates to the Form Fields page and verifies the form")
@allure.link("https://practice-automation.com/form-fields","Website")
@pytest.mark.parametrize("set_up_section", ["Form Fields"], indirect=True)
@pytest.mark.form
def test_form_fields(set_up_section):
    page = set_up_section
    form_fields_page = FormFieldsPage(page)
    
    form_fields_page.complete_form()
    form_fields_page.submit_form()
    form_fields_page.go_back()    
    form_fields_page.validate_title("Form Fields | automateNow | Practice")

