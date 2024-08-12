import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)

class Alertss:
    @staticmethod
    def handle_alert(driver, expected_text, timeout=20):
        try:
            alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            return alert_text
        except TimeoutException:
            return None
