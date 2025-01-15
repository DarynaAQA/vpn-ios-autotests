from base_classes.appium_methods import AppiumMethods
from locators.authorization_registration_locators import LoginLocators
from locators.main_locators import MainLocators
from dotenv import load_dotenv
import os
import datetime
import time


class AuthorizationRegistrationPage(AppiumMethods):

    def login_premium_user(self):
        load_dotenv()
        (self.is_clickable('accessibility_id', MainLocators.MainAccountButton).click())
        self.clear_element('accessibility_id', LoginLocators.EnterEmail)
        self.is_clickable('accessibility_id', LoginLocators.EnterEmail).send_keys(os.getenv("PREMIUM_EMAIL"))
        self.is_clickable('accessibility_id', LoginLocators.SignIn).click()
        self.clear_element('accessibility_id', LoginLocators.EnterPassword)
        time.sleep(4)
        (self.is_clickable('accessibility_id', LoginLocators.EnterPassword).
         send_keys(os.getenv("PREMIUM_PASSWORD")))
        self.is_clickable('accessibility_id', LoginLocators.SignIn).click()
        self.is_clickable('accessibility_id', LoginLocators.SignIn).click()

    def login_free_user(self):
        load_dotenv()
        (self.is_clickable('accessibility_id', MainLocators.MainAccountButton).click())
        self.clear_element('accessibility_id', LoginLocators.EnterEmail)
        self.is_clickable('accessibility_id', LoginLocators.EnterEmail).send_keys(os.getenv("FREE_EMAIL"))
        self.is_clickable('accessibility_id', LoginLocators.SignIn).click()
        self.clear_element('accessibility_id', LoginLocators.EnterPassword)
        time.sleep(4)
        (self.is_clickable('accessibility_id', LoginLocators.EnterPassword).send_keys(os.getenv("FREE_PASSWORD")))
        self.is_clickable('accessibility_id', LoginLocators.SignIn).click()
        self.is_clickable('accessibility_id', LoginLocators.SignIn).click()

    def registration(self):
        load_dotenv()
        self.is_clickable('accessibility_id', MainLocators.MainAccountButton).click()
        date_registration = datetime.datetime.now().strftime("%d%m%H%M")
        email = f"darina.test{date_registration}@gmail.com"
        self.is_clickable('accessibility_id', LoginLocators.EnterEmail).click()
        self.is_clickable('accessibility_id', LoginLocators.EnterEmail).send_keys(email)
        self.is_clickable('accessibility_id', LoginLocators.SignIn).click()

    def enter_email_for_authorization(self):
        load_dotenv()
        self.is_clickable('accessibility_id', MainLocators.MainAccountButton).click()
        self.is_clickable('accessibility_id', LoginLocators.EnterEmail).click()
        self.is_clickable('accessibility_id', LoginLocators.EnterEmail).send_keys(os.getenv("PREMIUM_EMAIL"))
        self.is_clickable('accessibility_id', LoginLocators.SignIn).click()

    def enter_email_field_click(self):
        load_dotenv()
        return (self.is_clickable('accessibility_id', LoginLocators.EnterEmail).
                send_keys(os.getenv("PREMIUM_EMAIL")))

    def sign_in_button_click(self):
        return self.is_clickable('accessibility_id', LoginLocators.SignIn).click()

    def enter_password_field_click(self):
        return self.is_clickable('accessibility_id', LoginLocators.SignIn).click()

    def understand_click(self):
        return self.is_present('accessibility_id', LoginLocators.IUnderstand).click()

    def check_presence_for_sign_in_title(self):
        return self.is_present('name', LoginLocators.SignInTitle)




