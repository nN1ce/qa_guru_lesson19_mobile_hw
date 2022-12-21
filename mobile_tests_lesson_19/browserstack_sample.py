from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",

    # Set URL of the application under test
    "app" : "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

    # Set other BrowserStack capabilities
    'bstack:options' : {
        "projectName" : "First Python project",
        "buildName" : "browserstack-build-DEMO",
        "sessionName" : "BStack first_test",

        # Set your access credentials
        "userName" : "viktoriam_BKTqwH",
        "accessKey" : "GwpKogsTijLksVhu6HNA"
    }
})

browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))
browser.quit()