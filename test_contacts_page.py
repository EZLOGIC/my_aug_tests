from .pages.contacts_page import ContactsPage
from .pages.login_page import LoginPage
from .pages.locators import ContactsPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time


link = "https://augmedix.com/contact-us/"


class TestContactsTable():
    
    "didn't execute 1st and 3rd test because didn't want \
    to send you forms with test data"
    
    def test_fill_all_required_fields(self, browser):
        page = ContactsPage(browser, link)   
        page.open()                      
        page.browser.switch_to.frame(ContactsPageLocators.IFRAME)
        page.send_last_name()
        page.send_job_title()
        page.choose_job_level()
        page.send_busyness_email()
        page.send_phone_number()
        page.choose_how_did_you_hear_about_augmedix()
        page.choose_request_type()
        time.sleep(5)

    def test_fill_only_unnecessary_fields(self, browser):
        page = ContactsPage(browser, link)   
        page.open()                      
        page.browser.switch_to.frame(ContactsPageLocators.IFRAME)
        page.send_first_name()
        button = page.browser.find_element(*ContactsPageLocators.SUBMIT)
        button.click()
        alert = WebDriverWait(page.browser, 10).until(
            EC.presence_of_element_located(ContactsPageLocators.ALERTMESSAGE)).text
        assert alert == "Please complete all required fields.", "Alerts shoukd be equal"
        
    def test_fill_all_fields(self, browser):
        page = ContactsPage(browser, link)   
        page.open()                      
        page.browser.switch_to.frame(ContactsPageLocators.IFRAME)
        page.send_first_name()
        page.send_last_name()
        page.send_job_title()
        page.choose_job_level()
        page.send_busyness_email()
        page.send_phone_number()
        page.choose_how_did_you_hear_about_augmedix()
        page.choose_request_type()
        time.sleep(5)

    
        
        
    

