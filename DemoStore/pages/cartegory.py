import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as explicitwait


class CartegoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.cartegory = (By.XPATH, '//*[@id="itemc"]')
        self.item = (By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
        self.cat_btn = (By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')

    def clickCartegory(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.cartegory)
        ).click()

    #click item
    def clickItem(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.item)
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.cat_btn)
        ).click()

