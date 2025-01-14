from base_classes.appium_methods import AppiumMethods
from base_classes.qase_integration import QASEIntegration
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.authorization_registration_page import AuthorizationRegistrationPage
from pages.sidebar_page import SidebarPage
from pages.advertising_page import AdvertisingPage
import time


class TestAuthorization:

    def test_authorization_free_user(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Launch app
            2. Click "Agree and Continue" button on the Privacy Policy screen
            3. Click "Allow" to send notifications from app
            4. Click "Continue for free" on the advertising window
            5. Authorize as a user with a Free subscription
        """
        appium_methods = AppiumMethods(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.login_free_user()
            main_methods.sidebar_button_click()
            name_subscription_plan = sidebar_methods.get_name_of_free_subscription_plan()
            assert name_subscription_plan == "Plan: Free"
            qase.create_passed_result(case=272, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=272, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Not found name of Free subscription plan  \n {ex}")

    def test_authorization_premium_user(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Launch app
            2. Click "Agree and Continue" button on the Privacy Policy screen
            3. Click "Allow" to send notifications from app
            4. Click "Continue for free" on the advertising window
            5. Authorize as a user with a Premium subscription
        """
        appium_methods = AppiumMethods(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.login_premium_user()
            main_methods.sidebar_button_click()
            name_subscription_plan = sidebar_methods.get_name_of_premium_subscription_plan()
            assert name_subscription_plan == "Plan: Premium"
            qase.create_passed_result(case=275, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=275, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Not found name of Premium subscription plan  \n {ex}")
