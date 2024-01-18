from .pages.base_page import BasePage
import pytest


@pytest.mark.parametrize('link', ["https://augmedix.com/augmedix-go/",
                                  "https://augmedix.com/augmedix-live/",
                                  "https://augmedix.com/augmedix-notes/",
                                  "https://augmedix.com/augmedix-prep/"])
class TestContactsPageRedirection():
    def test_guest_can_go_to_contacts_page(self, browser, link):
        page = BasePage(browser, link)   
        page.open()                      
        page.go_to_contacts_page()
        page.should_be_contacts_page()

    

