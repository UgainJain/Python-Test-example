import logging
import time

from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class LoginService:
    def __init__(self, driver):
        self.driver = driver
        self.login=LoginPage(self.driver)

    # login with valid credentials
    def login_valid(self, username, password):
        logger.info("Starting login test")
        self.login.clickLogin()
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.click_login_button()

    #login with invalid credentials
    def invalidlogin(self, username, password):
        logger.info("Starting login with invalid test")
        self.login.clickLogin()
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.click_login_button()
        self.login.closes()

    def is_shown(self):
        return self.login.available()
