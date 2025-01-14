from base_classes.appium_methods import AppiumMethods
from locators.sidebar_about_locators import AboutLocators


class AboutPage(AppiumMethods):

    def check_presence_for_about_title(self):
        return self.is_present('name', AboutLocators.AboutTitle)
