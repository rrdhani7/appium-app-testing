import pytest
import logging
from appium import webdriver as appium_driver
from selenium.webdriver import ActionChains


class TestApp:

    @classmethod
    def setup_class(cls):
        caps = {
            "platformName": "Android",
            "app": "/Users/dhani/Project/apk/new_scientists.apk",
            "deviceName": "emulator-5554",
            "appPackage": "com.newscientist.mobile",
            "appActivity": "com.kaldorgroup.pugpig.products.StartViewController"
        }
        cls.driver = appium_driver.Remote(
            command_executor="http://localhost:4723/wd/hub",
            desired_capabilities=caps
        )

    @pytest.mark.app
    def test_setup(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element_by_id("slideshow_close")
        logging.info(element)
        actions.move_to_element(element)
        actions.click()
        actions.perform()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
