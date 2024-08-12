import logging

from pages.cart import CartPage

logger = logging.getLogger(__name__)


class CartService:
    def __init__(self, driver):
        self.driver = driver
        self.cart = CartPage(self.driver)

    def click_order(self):
        logger.info("Starting cartegory test")
        self.cart.clickCart()
        self.cart.click_order_button()

    def is_available(self):
        return self.cart.available()
