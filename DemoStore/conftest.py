import json
import logging
import os
import time

import pytest
from selenium import webdriver
from datetime import datetime


def take_screenshot(web_driver, test_name):
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Creating a screenshot file name with timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_file = f"screenshots/{test_name}_{timestamp}.png"
    web_driver.save_screenshot(screenshot_file)


@pytest.fixture(scope="class")
def config_data():
    try:
        with open("Test_Data\config.json") as config_file:
            data = json.load(config_file)
            return data

    except FileNotFoundError:
        print("Couldn't find the file")


@pytest.fixture(scope="class")
def init_driver(request, config_data):
    global driver
    browser = config_data["browser"]
    headless = config_data["headless"]
    implicitwait = config_data["implicit"]
    url = config_data["url"]

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.implicitly_wait(implicitwait)
    driver.get(url)
    time.sleep(5)
    #driver accessible to test class
    request.cls.driver = driver
    yield
    driver.quit()



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call' and result.failed:
        web_driver = getattr(item.instance, 'driver', None)
        if web_driver:
            take_screenshot(web_driver, item.name)
        else:
            logging.error(" cannot take screenshot")


pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, "tests.log")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger()
