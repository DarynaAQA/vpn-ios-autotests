from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import Interaction
import datetime
from appium.options.ios import XCUITestOptions
from appium.webdriver.mobilecommand import MobileCommand
import time


class AppiumMethods:

    def __init__(self, driver):
        self.driver = driver
        self.time = time.time()
        self.wait = WebDriverWait(self.driver, 30, 0.5)
        self.bundle_id = "com.atrix.rusvpn"

    def get_appium_by(self, find_by: str):
        find_by = find_by.lower()
        locating_elements = {'xpath': AppiumBy.XPATH,
                             'class_name': AppiumBy.CLASS_NAME,
                             'id': AppiumBy.ID,
                             'link_text': AppiumBy.LINK_TEXT,
                             'name': AppiumBy.NAME,
                             'partial_link_text': AppiumBy.PARTIAL_LINK_TEXT,
                             'tag_name': AppiumBy.TAG_NAME,
                             'accessibility_id': AppiumBy.ACCESSIBILITY_ID}
        return locating_elements[find_by]

    def launch_app(self, bundle_id):
        self.driver.launch_app(bundle_id)

    def close_app(self, bundle_id):
        self.driver.terminate_app(bundle_id)

    def background_app(self):
        self.driver.background_app()

    def remove_app(self):
        self.driver.remove_app(self.bundle_id)

    def reset_app(self):
        return self.driver.reset()

    def quit_app(self):
        return self.driver.quit()

    def activate_app(self, bundle_id):
        return self.driver.activate_app(bundle_id)

    def is_present(self, find_by: str, locator: str) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((self.get_appium_by(find_by), locator)))

    def find_element(self, find_by: str, locator: str) -> WebElement:
        return self.driver.find_element(self.get_appium_by(find_by), locator)

    def clear_element(self, find_by: str, locator: str) -> WebElement:
        return self.driver.find_element(self.get_appium_by(find_by), locator).clear()

    def is_clickable(self, find_by: str, locator: str) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable((self.get_appium_by(find_by), locator)))

    def get_text_by_id(self, find_by: str, locator: str):
        return self.driver.find_element(self.get_appium_by(find_by), locator).get_attribute('name')

    def get_current_time(self):
        current_time = datetime.datetime.now()
        time_part = str(current_time).split()[1]
        time_without_ms = time_part.split('.')[0]
        hours, minutes, seconds = map(int, time_without_ms.split(':'))
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds

    def scroll(self, start_x: int, start_y: int, end_x: int, end_y: int):
        """Perform scroll by given coordinates"""
        self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def scroll_to_element(self, find_by: str, locator: str, max_scrolls) -> WebElement:
        self.is_present(find_by, locator)
        for _ in range(max_scrolls):
            try:
                elem = self.is_clickable(find_by, locator)
            except TimeoutException:
                self.scroll(300, 2800, 300, 700)
                pass
            else:
                return elem

    def tap_by_coordinates(self, x: int, y: int):
        return self.driver.tap([(x, y)])

    def open_browser(self):
        return self.activate_app('com.apple.mobilesafari')

    def close_browser(self):
        return self.close_app('com.apple.mobilesafari')

    def background_app_planet(self):
        return self.driver.background_app(-1)

    def open_url(self, url: str):
        return self.driver.get(url)

    def get_element_text(self, find_by: str, locator: str):
        """
            This method get text from web element on the page.
        """
        return self.driver.find_element(self.get_appium_by(find_by), locator).text

    def mobile_tap_element(self, find_by: str, locator: str):
        return self.driver.execute_script('mobile: tap', {self.get_appium_by(find_by), locator})








































