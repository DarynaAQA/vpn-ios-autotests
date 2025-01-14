from base_classes.appium_methods import AppiumMethods
from locators.main_locators import MainLocators
from locators.pop_up_locators import PopUpLocators
import json


class ConnectionToVpnPage(AppiumMethods):

    def check_presence_for_disconnect_button(self):
        return self.is_present('accessibility_id', MainLocators.DisconnectButton)

    def disconnect_button_click(self):
        return self.is_clickable('accessibility_id', MainLocators.DisconnectButton).click()

    def click_ok_button_on_pop_up(self):
        return self.is_clickable('accessibility_id', PopUpLocators.OkButton).click()

    def check_presence_for_pop_up(self):
        return self.is_present('accessibility_id', PopUpLocators.TextPopUp)

    def get_current_ip_address(self):
        self.driver.refresh('https://ipinfo.io/json')
        ip_element = self.find_element('xpath', '//XCUIElementTypeWebView[@name="WebView"]/XCUIElement'
                                                'TypeWebView/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElement'
                                                'TypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElement'
                                                'TypeOther/XCUIElementTypeStaticText').text
        return json.loads(ip_element).get('ip')

    def clear_premium_results_file(self):
        with open('results_connection_premium_servers.txt', 'w') as file:
            pass

    def clear_free_results_file(self):
        with open('results_connection_free_servers.txt', 'w') as file:
            pass













