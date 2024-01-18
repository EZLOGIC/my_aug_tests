from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_url(self):
        assert "ee-portal" in self.browser.current_url, "Login url is not presented"

