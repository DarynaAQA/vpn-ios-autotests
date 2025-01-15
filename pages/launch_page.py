from base_classes.appium_methods import AppiumMethods
from locators.launch_locators import LaunchLocators


class LaunchPage(AppiumMethods):
    def check_presence_for_logo(self):
        return self.is_present('accessibility_id', LaunchLocators.LogoVpn)

    def check_presence_for_name_app(self):
        return self.is_present('accessibility_id', LaunchLocators.NameApp)

    def check_presence_for_launch_loader(self):
        return self.is_present('accessibility_id', LaunchLocators.LaunchLoader)


