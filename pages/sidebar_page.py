from base_classes.appium_methods import AppiumMethods
from locators.sidebar_locators import SidebarLocators


class SidebarPage(AppiumMethods):

    def get_name_of_premium_subscription_plan(self):
        return self.get_text_by_id('accessibility_id', SidebarLocators.SubscriptionPlanPremium)

    def get_name_of_free_subscription_plan(self):
        return self.get_text_by_id('accessibility_id', SidebarLocators.SubscriptionPlanFree)

    def check_presence_for_free_plan(self):
        return self.is_present('accessibility_id', SidebarLocators.SubscriptionPlanFree)

    def check_presence_for_premium_plan(self):
        return self.is_present('accessibility_id', SidebarLocators.SubscriptionPlanPremium)

    def check_for_presence_settings(self):
        return self.is_present('accessibility_id', SidebarLocators.SettingsButton)

    def click_settings_button(self):
        return self.is_clickable('accessibility_id', SidebarLocators.SettingsButton).click()

    def check_for_presence_subscription_plans(self):
        return self.is_present('accessibility_id', SidebarLocators.SubscriptionPlans)

    def click_subscription_plans_button(self):
        return self.is_clickable('accessibility_id', SidebarLocators.SubscriptionPlans).click()

    def check_for_presence_faq_support(self):
        return self.is_present('accessibility_id', SidebarLocators.FAQSupport)

    def click_faq_support_button(self):
        return self.is_clickable('accessibility_id', SidebarLocators.FAQSupport).click()

    def check_for_presence_rate_app(self):
        return self.is_present('accessibility_id', SidebarLocators.RateApp)

    def check_for_presence_share(self):
        return self.is_present('accessibility_id', SidebarLocators.ShareButton)

    def click_share_button(self):
        return self.is_clickable('accessibility_id', SidebarLocators.ShareButton).click()

    def check_for_presence_about_button(self):
        return self.is_present('accessibility_id', SidebarLocators.AboutButton)

    def click_about_button(self):
        return self.is_clickable('accessibility_id', SidebarLocators.AboutButton).click()

    def check_for_presence_sign_in(self):
        return self.is_present('name', SidebarLocators.SignIn)

    def sign_in_button_click(self):
        return self.is_clickable('name', SidebarLocators.SignIn).click()

    def check_for_presence_logout_button(self):
        return self.is_present('name', SidebarLocators.LogOut)

    def click_logout_button(self):
        return self.is_clickable('name', SidebarLocators.LogOut).click()

    def check_for_presence_manage_button(self):
        return self.is_present('name', SidebarLocators.Manage)

    def click_manage_button(self):
        return self.is_clickable('name', SidebarLocators.Manage).click()

    def check_for_presence_get_premium_button(self):
        return self.is_present('name', SidebarLocators.GetPremium)

    def get_premium_button_click(self):
        return self.is_clickable('name', SidebarLocators.GetPremium).click()

    def click_back_button(self):
        return self.is_clickable('accessibility_id', SidebarLocators.BackButton).click()

    def check_presence_for_confirmation_log_out(self):
        return self.is_present('accessibility_id', SidebarLocators.ConfirmationLogOut)

    def check_presence_for_sign_in_title(self):
        return self.is_present('xpath', SidebarLocators.SignInTitle)








