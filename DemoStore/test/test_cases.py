import logging
import time

import pytest
import json

from BusinessLayer.cart_service import CartService
from BusinessLayer.cartegory_service import CartegoryService
from BusinessLayer.login_service import LoginService
from BusinessLayer.order_service import OrderService
from BusinessLayer.signup_service import SignUpBusinessLayer
from Utils.alerts import Alertss

#from Utils.logginga import get_logger


logger = logging.getLogger(__name__)
@pytest.mark.usefixtures("init_driver")
class TestAuth:

    @pytest.fixture(autouse=True)
    def setup(self, init_driver):
        #self.logger = get_logger(__name__)
        self.login = LoginService(self.driver)
        self.signup = SignUpBusinessLayer(self.driver)
        self.cartegory = CartegoryService(self.driver)
        self.cart = CartService(self.driver)
        self.order = OrderService(self.driver)

    @pytest.fixture(scope="class")
    def get_data(self):
        try:
            with open("Test_Data\config.json") as config_file:
                data = json.load(config_file)
                return data
        except FileNotFoundError:
            print("Couldn't find the file")

    #testing creation of new account
    def test_singup(self, get_data):
        signup_data = get_data["signup_data"]
        alerts = get_data["signupAlert"]
        self.signup.signup(signup_data["username"], signup_data["password"])
        alert_text = Alertss.handle_alert(self.driver, alerts)
        assert alert_text == alerts
        logger.info("Finished signup test case process")


    def test_login(self, get_data):
        login_data = get_data["login_data"]
        self.login.login_valid(login_data["username"], login_data["password"])

        assert self.login.is_shown(), "User name displayed"
        logger.info(f"Login successful, username {login_data['username']} is displayed")
        logger.info("Finished login test case process")
        # Navigate back to url for other tests
        self.driver.get(get_data["url"])

    def test_invalidcredentials(self, get_data):
        login_data = get_data["invalid_data"]
        alerts = get_data["login_alert"]
        self.login.invalidlogin(login_data["username"], login_data["password"])
        logger.info(f"Login unsuccessful, alert is displayed")
        #assert  the alert is available
        alert_text = Alertss.handle_alert(self.driver, alerts)
        assert alert_text == alerts
        logger.info("Finished login test case process")

    def test_category_and_add_to_cart(self, get_data):
        alerts = get_data["cart_alert"]
        time.sleep(2)
        self.cartegory.select_cartegory()
        #show alert
        alert_text = Alertss.handle_alert(self.driver, alerts)
        assert alert_text == alerts
        logger.info("Added item to cart alert received")
        logger.info("Finished cart and category test case process")

    def test_order(self):
        time.sleep(2)
        self.cart.click_order()
        #assert the item is available
        assert self.cart.is_available(), "Item available"
        logger.info("Item Available in cart")

    def test_createpurchase(self, get_data):
        # order data
        order_data = get_data["User_Details"]
        self.order.create_order(order_data["name"], order_data["country"], order_data["city"], order_data["card"],
                                order_data["month"],
                                order_data["year"])
        time.sleep(2)
        assert self.order.Is_Shown()
        logger.info("User order sucessful")
        logger.info("Finished order  test case process")
