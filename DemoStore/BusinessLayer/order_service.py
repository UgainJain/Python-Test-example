import logging

from pages.Order_page import OrderPage
from pages.cart import CartPage

logger = logging.getLogger(__name__)


class OrderService:
    def __init__(self, driver):
        self.driver = driver
        self.order=OrderPage(self.driver)

    def create_order(self,name,country,city,card,month,year):
        logger.info("Starting order test")
        self.order.names(name)
        self.order.countries(country)
        self.order.cities(city)
        self.order.cards(card)
        self.order.months(month)
        self.order.years(year)
        self.order.click_purchace()

    def Is_Shown(self):
        return self.order.IsAvailable()
