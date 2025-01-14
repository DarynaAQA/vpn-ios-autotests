from base_classes.appium_methods import AppiumMethods
from base_classes.qase_integration import QASEIntegration
from pages.advertising_page import AdvertisingPage
from selenium.webdriver.remote.webelement import WebElement
from pages.privacy_policy_page import PrivacyPolicyPage


class TestPrivacyPolicy:

    def test_privacy_policy_accept(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click on the "Agree and Continue" button on the Privacy Policy screen
        """
        appium_methods = AppiumMethods(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            continue_for_free_button = advertising_methods.check_presence_for_free_button()
            assert isinstance(continue_for_free_button, WebElement)
            qase.create_passed_result(case=87, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=87, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Continue for free button not found \n {ex}")

    def test_decline_privacy_policy(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click on the "X" button on Privacy Policy screen
        """
        appium_methods = AppiumMethods(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.decline_privacy_policy()
            qase.create_passed_result(case=88, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=88, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Click on close button is not successful \n {ex}")

    def test_privacy_policy_link(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click on the Privacy Policy link
        """
        appium_methods = AppiumMethods(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.privacy_policy_link_click()
            privacy_policy_header = privacy_policy_methods.check_for_presence_privacy_policy_header()
            assert isinstance(privacy_policy_header, WebElement)
            qase.create_passed_result(case=89, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=89, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Privacy policy header not found \n {ex}")
