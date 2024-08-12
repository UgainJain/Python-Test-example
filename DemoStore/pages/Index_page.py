from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as explicitwait


class SinUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.SinUP_link = (By.ID, "signin2")
        self.username = (By.ID, "sign-username")
        self.password = (By.ID, "sign-password")
        self.signup_button = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
        self.close = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[1]')

    def clickSign(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.SinUP_link)
        ).click()

    #enter username in field
    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            explicitwait.visibility_of_element_located(self.username)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            explicitwait.visibility_of_element_located(self.password)
        ).send_keys(password)

    def click_signup_button(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.signup_button)
        ).click()

    def closes(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.close)
        ).click()
