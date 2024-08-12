import logging

logger = logging.getLogger(__name__)

from pages.Index_page import SinUpPage


class SignUpBusinessLayer:

    def __init__(self, driver):
        self.driver = driver

    def signup(self, username, password):
        logger.info("Starting signup test")
        signup_page = SinUpPage(self.driver)
        signup_page.clickSign()
        signup_page.enter_username(username)
        signup_page.enter_password(password)
        signup_page.click_signup_button()
        signup_page.closes()



