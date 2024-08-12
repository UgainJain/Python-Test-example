import logging

from pages.cartegory import CartegoryPage

logger = logging.getLogger(__name__)


class CartegoryService:
    def __init__(self, driver):
        self.driver = driver

    def select_cartegory(self):
        logger.info("Starting category test")
        category = CartegoryPage(self.driver)
        category.clickCartegory()
        category.clickItem()
