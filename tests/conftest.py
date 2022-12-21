import os
import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from appium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options

from mobile_tests_lesson_19.assist import attach


#from wikipedia.util import attachments


@pytest.fixture(scope='session', autouse=True)
def driver_management():
    load_dotenv()
    USER_NAME = 'bsuser_lS1iZg'
    ACCESS_KEY = '4FdkNSy1s5WWMvarKD2q'
    APP = 'bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c'
    PLATFORM_NAME = "Test"
    options = UiAutomator2Options()

    options.load_capabilities({
        "app": f"{APP}",
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",
        "platformName": f"{PLATFORM_NAME}",
        "project": "Python project",
        "build": "wikipedia-build-qa_guru",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-DEMO",
            "sessionName": "BStack first_test",
            "userName": f"{USER_NAME}",
            "accessKey": f"{ACCESS_KEY}",
        }
    })
    browser.config.driver = webdriver.Remote(
        command_executor="http://hub.browserstack.com/wd/hub",
        options=options,
    )
    browser.config.timeout = 4
    yield driver_management
    attach.add_video(browser)
    browser.quit()