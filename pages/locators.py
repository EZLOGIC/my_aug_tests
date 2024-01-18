from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "[class^='signinbutton'] a")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CONTACTS_LINK = (By.CSS_SELECTOR,
                    "[class*='et_pb_column_3_5 et_pb_column_0'] :nth-child(3) a")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login-panel.white-oberlay")
    EMAIL = (By.CSS_SELECTOR, "#login-email")
    PASSWORD = (By.CSS_SELECTOR, "[name='password']")
    SIGN_IN = (By.CSS_SELECTOR, ".btnlogin [type='submit']")

    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "[class^='signinbutton'] a")


class ContactsPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "[class^='signinbutton'] a")
    IFRAME = ("hs-form-iframe-0")
    FIRSTNAME = (By.XPATH, "//input[@name='firstname']")
    LASTNAME = (By.XPATH, "//input[@name='lastname']")
    JOB_TITLE = (By.XPATH, "//input[@name='jobtitle']")
    JOB_LEVEL = (By.XPATH, "//select[@name='job_level']")
    EMAIL = (By.XPATH, "//input[starts-with(@id, 'email')]")
    PHONE = (By.XPATH, "//input[contains(@id, 'phone')]")
    REQUEST_TYPE = (By.XPATH, "//select[@name='request_type']")
    SUBMIT = (By.XPATH, "//input[@type='submit']")
    ALERTMESSAGE = (By.XPATH, "//label[@class='hs-main-font-element']")
    
    
    
