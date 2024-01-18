from .pages.contacts_page import ContactsPage
from .pages.login_page import LoginPage
from .pages.locators import ContactsPageLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


link = "https://augmedix.com/contact-us/"


class TestContactsTable():
    
    "didn't execute 1st and 3rd test because didn't want \
    to send you forms with test data"
    
    """def test_fill_all_required_fields(self, browser):
        page = ConatctsPage(browser, link)   
        page.open()                      
        page.browser.switch_to.frame(ContactsPageLocators.IFRAME)
        lastname = page.browser.find_element(*ContactsPageLocators.LASTNAME)
        lastname.send_keys('Smith')
        job_title = page.browser.find_element(*ContactsPageLocators.JOB_TITLE)
        job_title.send_keys('King')
        job_level = Select(browser.find_element(*ContactsPageLocators.JOB_LEVEL))
        job_level.select_by_index(3)
        busyness_email = page.browser.find_element(*ContactsPageLocators.EMAIL)
        busyness_email.send_keys('esytest1@gmail.com')
        phone_number = page.browser.find_element(*ContactsPageLocators.PHONE)
        phone.number.send_keys('1111111111')
        request_type = Select(browser.find_element(
            *ContactsPageLocators.REQUEST_TYPE))
        request_type.select_by_index(3)
        button = page.browser.find_element(*ContactsPageLocators.SUBMIT)
        button.click()"""

    def test_fill_only_unnecessary_fields(self, browser):
        page = ContactsPage(browser, link)   
        page.open()                      
        page.browser.switch_to.frame(ContactsPageLocators.IFRAME)
        firstname = page.browser.find_element(*ContactsPageLocators.FIRSTNAME)
        firstname.send_keys('Alex')
        button = page.browser.find_element(*ContactsPageLocators.SUBMIT)
        button.click()
        alert = WebDriverWait(page.browser, 10).until(
            EC.presence_of_element_located(ContactsPageLocators.ALERTMESSAGE)).text
        assert alert == "Please complete all required fields.", "Alerts shoukd be equal"
        
    """def test_fill_all_fields(self, browser):
        page = ConatctsPage(browser, link)   
        page.open()                      
        page.browser.switch_to.frame(ContactsPageLocators.IFRAME)
        firstname = page.browser.find_element(*ContactsPageLocators.FIRSTNAME)
        firstname.send_keys('Alex')
        lastname = page.browser.find_element(*ContactsPageLocators.LASTNAME)
        lastname.send_keys('Smith')
        job_title = page.browser.find_element(*ContactsPageLocators.JOB_TITLE)
        job_title.send_keys('King')
        job_level = Select(browser.find_element(*ContactsPageLocators.JOB_LEVEL))
        job_level.select_by_index(3)
        busyness_email = page.browser.find_element(*ContactsPageLocators.EMAIL)
        busyness_email.send_keys('esytest1@gmail.com')
        phone_number = page.browser.find_element(*ContactsPageLocators.PHONE)
        phone.number.send_keys('1111111111')
        request_type = Select(browser.find_element(
            *ContactsPageLocators.REQUEST_TYPE))
        request_type.select_by_index(3)
        button = page.browser.find_element(*ContactsPageLocators.SUBMIT)
        button.click()"""

    
        
        
    

