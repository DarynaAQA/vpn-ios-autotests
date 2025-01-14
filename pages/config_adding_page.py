from base_classes.appium_methods import AppiumMethods
from locators.config_adding_locators import ConfigAddingLocators


class ConfigAddingPage(AppiumMethods):

    def got_it_button_click(self):
        return self.is_clickable('accessibility_id', ConfigAddingLocators.GotItButton).click()

    def check_presence_for_info_about_permission(self):
        return self.is_present('accessibility_id', ConfigAddingLocators.WeNeedPermission)
