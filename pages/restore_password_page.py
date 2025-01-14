from base_classes.appium_methods import AppiumMethods
from locators.restore_password_locators import RestorePasswordLocators


class RestorePasswordPage(AppiumMethods):

    def reset_button_click(self):
        return self.is_present('accessibility_id', RestorePasswordLocators.ResetButton).click()

    def check_for_presence_send_email_notification(self):
        return self.is_present('accessibility_id', RestorePasswordLocators.SendEmailNotification)

    def ok_button_click(self):
        return self.is_present('accessibility_id', RestorePasswordLocators.OkButton).click()

    def restore_password_button_click(self):
        return self.is_clickable('accessibility_id', RestorePasswordLocators.RestorePasswordButton).click()







