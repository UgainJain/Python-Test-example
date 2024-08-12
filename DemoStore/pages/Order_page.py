from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as explicitwait


class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.name = (By.ID, "name")
        self.country = (By.ID, "country")
        self.city = (By.ID, "city")
        self.card = (By.ID, "card")
        self.month = (By.ID, "month")
        self.year = (By.ID, "year")
        self.buttnPurchase = (By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
        self.num = (By.XPATH, '/html/body/div[10]/h2')

    #enter user details
    def names(self, username):
        WebDriverWait(self.driver, 5).until(
            explicitwait.visibility_of_element_located(self.name)
        ).send_keys(username)

    def countries(self, c):
        WebDriverWait(self.driver, 5).until(
            explicitwait.visibility_of_element_located(self.country)
        ).send_keys(c)

    def cities(self, c):
        WebDriverWait(self.driver, 5).until(
            explicitwait.visibility_of_element_located(self.city)
        ).send_keys(c)

    def cards(self, c):
        WebDriverWait(self.driver, 5).until(
            explicitwait.visibility_of_element_located(self.card)
        ).send_keys(c)

    def months(self, c):
        WebDriverWait(self.driver, 5).until(
            explicitwait.visibility_of_element_located(self.month)
        ).send_keys(c)


    def years(self, c):
        WebDriverWait(self.driver, 5).until(
            explicitwait.visibility_of_element_located(self.year)
        ).send_keys(c)

    def click_purchace(self):
        WebDriverWait(self.driver, 5).until(
            explicitwait.visibility_of_element_located(self.buttnPurchase)
        ).click()

    def IsAvailable(self):
        return WebDriverWait(self.driver, 5).until(
            explicitwait.presence_of_element_located(self.num)
        )
