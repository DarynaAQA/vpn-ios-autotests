from base_classes.appium_methods import AppiumMethods
from locators.launch_locators import LaunchLocators
from locators.advertising_locators import AdvertisingLocators


class AdvertisingPage(AppiumMethods):

    def check_presence_for_free_button(self):
        return self.is_present('accessibility_id', AdvertisingLocators.ContinueForFreeButton)

    def continue_for_free_button_click(self):
        return self.is_clickable('accessibility_id', AdvertisingLocators.ContinueForFreeButton).click()



