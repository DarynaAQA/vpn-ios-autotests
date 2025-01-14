from base_classes.appium_methods import AppiumMethods
from base_classes.qase_integration import QASEIntegration
from pages.main_page import MainPage
from pages.advertising_page import AdvertisingPage
from pages.privacy_policy_page import PrivacyPolicyPage
from selenium.webdriver.remote.webelement import WebElement
from pages.authorization_registration_page import AuthorizationRegistrationPage
from pages.sidebar_subscriptions_page import SubscriptionsPage
from pages.benefits_premium_page import BenefitsPremiumPage
import time


class TestBenefitsPremium:

    def test_click_select_plan(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click on "Agree and Continue" button on the Privacy Policy screen
            4. Click on "Allow" to send notifications from app
            5. Click on "Continue for free" on the advertising window
            6. Click on Remove ads button
            7. Click on Select plan button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        subscriptions_methods = SubscriptionsPage(create_ios_driver)
        benefits_premium_methods = BenefitsPremiumPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.login_free_user()
            main_methods.remove_ads_button_click()
            benefits_premium_methods.select_plan_click()
            one_year = subscriptions_methods.check_for_presence_one_year()
            six_months = subscriptions_methods.check_for_presence_six_months()
            one_month = subscriptions_methods.check_for_presence_one_month()
            assert isinstance(one_year, WebElement), f"{one_year}"
            assert isinstance(six_months, WebElement), f"{six_months}"
            assert isinstance(one_month, WebElement), f"{one_month}"
            qase.create_passed_result(case=290, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=290, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Subscription plan not found \n {ex}")
