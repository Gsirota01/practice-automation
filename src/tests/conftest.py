import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.home_page import HomePage
from pages.form_fields_page import FormFieldsPage
from base.browser import set_up,set_up_section