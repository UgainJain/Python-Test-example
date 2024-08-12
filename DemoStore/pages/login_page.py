from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as explicitwait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.Login_Link = (By.XPATH, '//*[@id="login2"]')
        self.username = (By.ID, "loginusername")
        self.passw = (By.ID, "loginpassword")
        self.logB = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        self.closebtn = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[1]')
        self.name = (By.ID, "nameofuser")

    def clickLogin(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.Login_Link)
        ).click()

    #enter username in field
    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            explicitwait.visibility_of_element_located(self.username)
        ).send_keys(username)

    # enter password in field
    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            explicitwait.visibility_of_element_located(self.passw)
        ).send_keys(password)

    # enter click login button
    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.logB)
        ).click()

    def available(self):
        return WebDriverWait(self.driver, 10).until(
            explicitwait.presence_of_element_located(self.name)
        )

    def closes(self):
        WebDriverWait(self.driver, 10).until(
            explicitwait.element_to_be_clickable(self.closebtn)
        ).click()
