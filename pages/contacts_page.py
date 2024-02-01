from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .locators import ContactsPageLocators
from .login_page import LoginPage
import time

class ContactsPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*ContactsPageLocators.LOGIN_LINK)
        login_link.click()
        
    def should_be_login_link(self):
        assert self.is_element_present(*ContactsPageLocators.LOGIN_LINK), "Login link is not presented"

    def send_first_name(self):
        firstname = self.browser.find_element(*ContactsPageLocators.FIRSTNAME)
        firstname.send_keys('Alex')

    def send_last_name(self):
        lastname = self.browser.find_element(*ContactsPageLocators.LASTNAME)
        lastname.send_keys('Smith')

    def send_job_title(self):
        job_title = self.browser.find_element(*ContactsPageLocators.JOB_TITLE)
        job_title.send_keys('King')

    def choose_job_level(self):
        job_level = Select(self.browser.find_element(*ContactsPageLocators.JOB_LEVEL))
        job_level.select_by_index(3)

    def send_busyness_email(self):
        busyness_email = self.browser.find_element(*ContactsPageLocators.EMAIL)
        busyness_email.send_keys('esytest1@gmail.com')

    def send_phone_number(self):
        phone_number = self.browser.find_element(*ContactsPageLocators.PHONE)
        phone_number.send_keys('1111111111')

    def choose_how_did_you_hear_about_augmedix(self):
        request_type = Select(self.browser.find_element(
            *ContactsPageLocators.HOW_DID_YOU_HEAR))
        request_type.select_by_index(3)

    def choose_request_type(self):
        request_type = Select(self.browser.find_element(
            *ContactsPageLocators.REQUEST_TYPE))
        request_type.select_by_index(3)
