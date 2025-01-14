from base_classes.appium_methods import AppiumMethods
from locators.sidebar_faq_support_locators import FaqSupportLocators


class FaqSupportPage(AppiumMethods):

    def check_presence_for_faq_support_title(self):
        return self.is_present('name', FaqSupportLocators.FaqSupportTitle)
