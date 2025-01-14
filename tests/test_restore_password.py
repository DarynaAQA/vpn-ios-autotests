from base_classes.appium_methods import AppiumMethods
from base_classes.qase_integration import QASEIntegration
from pages.authorization_registration_page import AuthorizationRegistrationPage
from appium.webdriver import WebElement
from pages.restore_password_page import RestorePasswordPage
from pages.advertising_page import AdvertisingPage
from pages.privacy_policy_page import PrivacyPolicyPage
import time


class TestRestorePassword:

    def test_restore_password(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Allow" to send notifications from app
            5. Click "Continue for free" on the advertising window
            6. Click on the Account icon on the main screen
            7. Enter email for Restore password
            8. Click on Sign in
            9. Click on Restore password
            10. Click on Reset button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        restore_password_methods = RestorePasswordPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.enter_email_for_authorization()
            restore_password_methods.restore_password_button_click()
            restore_password_methods.reset_button_click()
            send_email_notification = restore_password_methods.check_for_presence_send_email_notification()
            assert isinstance(send_email_notification, WebElement)
            qase.create_passed_result(case=267, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=267, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Email notification not found \n {ex}")





