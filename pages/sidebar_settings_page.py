from base_classes.appium_methods import AppiumMethods
from locators.sidebar_settings_locators import SettingsLocators


class SettingsPage(AppiumMethods):

    def check_presence_for_settings_title(self):
        return self.is_present('name', SettingsLocators.SettingsTitle)
