from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as explicitwait


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.ID, "cartur")
        self.orderBTN = (By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
        self.item = (By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')

    def clickCart(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.cart_items)
        ).click()

    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.orderBTN)
        ).click()

    def available(self):
        return WebDriverWait(self.driver, 10).until(
            explicitwait.presence_of_element_located(self.item)
        )
