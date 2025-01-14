from base_classes.appium_methods import AppiumMethods
from locators.privacy_policy_locators import PrivacyPolicyLocators


class PrivacyPolicyPage(AppiumMethods):

    def accept_privacy_policy(self):
        return self.is_present('accessibility_id', PrivacyPolicyLocators.AgreeContinueButton).click()

    def decline_privacy_policy(self):
        return self.is_present('accessibility_id', PrivacyPolicyLocators.XButton).click()

    def privacy_policy_link_click(self):
        return self.is_present('accessibility_id', PrivacyPolicyLocators.PrivacyPolicyLink).click()

    def check_for_presence_logo(self):
        return self.is_present('accessibility_id', PrivacyPolicyLocators.LogoPlanetVpn)

    def check_for_presence_privacy_policy_header(self):
        return self.is_clickable('xpath', PrivacyPolicyLocators.PrivacyPolicyHeader)













