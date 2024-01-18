from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import ContactsPageLocators
from .login_page import LoginPage
import time

class ContactsPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*ContactsPageLocators.LOGIN_LINK)
        login_link.click()
        
    def should_be_login_link(self):
        assert self.is_element_present(*ContactsPageLocators.LOGIN_LINK), "Login link is not presented"
