from base_classes.appium_methods import AppiumMethods
from locators.main_locators import MainLocators


class MainPage(AppiumMethods):

    def check_presence_for_sidebar_button(self):
        return self.is_present('accessibility_id', MainLocators.SideBarButton)

    def get_name_current_location(self):
        return self.is_present('xpath', '//XCUIElementTypeButton[@name="MainChoose'
                                                'ServerButton"]/XCUIElementTypeStaticText[3]').get_attribute('value')

    def check_presence_for_app_name(self):
        return self.is_present('accessibility_id', MainLocators.PlanetVpnName)

    def check_presence_for_account_button(self):
        return self.is_present('accessibility_id', MainLocators.MainAccountButton)

    def check_presence_for_select_location_button(self):
        return self.is_present('accessibility_id', MainLocators.SelectLocation)

    def check_presence_for_logout_button(self):
        return self.is_present('accessibility_id', MainLocators.LogOutButton)

    def check_presence_for_your_location(self):
        return self.is_present('accessibility_id', MainLocators.YourLocation)

    def check_presence_for_protect_icon(self):
        return self.is_present('accessibility_id', MainLocators.IconNotProtected)

    def check_presence_for_protect_status(self):
        return self.is_present('accessibility_id', MainLocators.StatusNotProtected)

    def check_presence_for_connect_button(self):
        return self.is_present('accessibility_id', MainLocators.ConnectButton)

    def check_presence_for_remove_ads_button(self):
        return self.is_present('accessibility_id', MainLocators.RemoveAdsButton)

    def check_presence_for_ads_banner(self):
        return self.is_present('accessibility_id', MainLocators.DefaultAdsBanner)

    def check_presence_for_planet_animation(self):
        return self.is_present('accessibility_id', MainLocators.PlanetAnimation)

    def sidebar_button_click(self):
        return self.is_clickable('accessibility_id', MainLocators.SideBarButton).click()

    def select_location_button_click(self):
        return self.is_clickable('accessibility_id', MainLocators.SelectLocation).click()

    def connect_button_click(self):
        return self.is_clickable('accessibility_id', MainLocators.ConnectButton).click()

    def disconnect_button_click(self):
        return self.is_clickable('accessibility_id', MainLocators.ConnectButton).click()

    def remove_ads_button_click(self):
        return self.is_clickable('accessibility_id', MainLocators.RemoveAdsButton).click()














