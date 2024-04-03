import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os
import config
from qa_guru_python_21.utils import attach_allure
from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # 'platformName': 'android',
        'platformVersion': '9.0',
        'deviceName': 'Google Pixel 3',

        # Set URL of the application under test
        'app': 'bs://sample.app',

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Set your access credentials
            'userName': config.USER_APP,
            'accessKey': config.PASSWORD_APP,
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub', options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    session_id = browser.driver.session_id
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield
    attach_allure.bstack_screenshot()
    attach_allure.bstack_page_source()

    with allure.step('tear down app session'):
        browser.quit()
    attach_allure.bstack_video(session_id)
