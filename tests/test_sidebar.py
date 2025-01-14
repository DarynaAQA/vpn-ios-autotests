import time

from base_classes.appium_methods import AppiumMethods
from base_classes.qase_integration import QASEIntegration
from pages.main_page import MainPage
from pages.sidebar_page import SidebarPage
from pages.advertising_page import AdvertisingPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.authorization_registration_page import AuthorizationRegistrationPage
from pages.sidebar_settings_page import SettingsPage
from pages.sidebar_subscriptions_page import SubscriptionsPage
from pages.sidebar_faq_support_page import FaqSupportPage
from pages.sidebar_about_page import AboutPage
from selenium.webdriver.remote.webelement import WebElement


class TestSidebar:

    def test_check_for_presence_elements_in_sidebar_menu_free_user(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Click on the Sidebar menu button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            main_methods.sidebar_button_click()
            settings_button = sidebar_methods.check_for_presence_settings()
            faq_support_button = sidebar_methods.check_for_presence_faq_support()
            subscription_plans_button = sidebar_methods.check_for_presence_subscription_plans()
            share_button = sidebar_methods.check_for_presence_share()
            rate_app_button = sidebar_methods.check_for_presence_rate_app()
            about_button = sidebar_methods.check_for_presence_about_button()
            sign_in_button = sidebar_methods.check_for_presence_sign_in()
            free_plan = sidebar_methods.check_presence_for_free_plan()
            get_premium = sidebar_methods.check_for_presence_get_premium_button()
            assert isinstance(settings_button, WebElement)
            assert isinstance(faq_support_button, WebElement)
            assert isinstance(subscription_plans_button, WebElement)
            assert isinstance(share_button, WebElement)
            assert isinstance(rate_app_button, WebElement)
            assert isinstance(about_button, WebElement)
            assert isinstance(sign_in_button, WebElement)
            assert isinstance(free_plan, WebElement)
            assert isinstance(get_premium, WebElement)
            qase.create_passed_result(case=241, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=241, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Elements of sidebar menu not found for free user \n {ex}")

    def test_check_for_presence_elements_in_sidebar_menu_premium_user(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Log in as a premium user
            6. Click on the Sidebar menu button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.login_premium_user()
            main_methods.sidebar_button_click()
            settings_button = sidebar_methods.check_for_presence_settings()
            faq_support_button = sidebar_methods.check_for_presence_faq_support()
            subscription_plans_button = sidebar_methods.check_for_presence_subscription_plans()
            share_button = sidebar_methods.check_for_presence_share()
            rate_app_button = sidebar_methods.check_for_presence_rate_app()
            about_button = sidebar_methods.check_for_presence_about_button()
            log_out_button = sidebar_methods.check_for_presence_logout_button()
            manage_button = sidebar_methods.check_for_presence_manage_button()
            premium_plan = sidebar_methods.check_presence_for_premium_plan()
            assert isinstance(settings_button, WebElement)
            assert isinstance(faq_support_button, WebElement)
            assert isinstance(subscription_plans_button, WebElement)
            assert isinstance(share_button, WebElement)
            assert isinstance(rate_app_button, WebElement)
            assert isinstance(about_button, WebElement)
            assert isinstance(log_out_button, WebElement)
            assert isinstance(manage_button, WebElement)
            assert isinstance(premium_plan, WebElement)
            qase.create_passed_result(case=278, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=278, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Elements of sidebar menu not found for premium user \n {ex}")

    def test_click_settings_button(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Click on the Sidebar menu button
            6. Click on the Settings button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        settings_methods = SettingsPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            main_methods.sidebar_button_click()
            sidebar_methods.click_settings_button()
            settings_title = settings_methods.check_presence_for_settings_title()
            assert isinstance(settings_title, WebElement)
            qase.create_passed_result(case=14, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=14, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Settings title not found \n {ex}")

    def test_click_subscription_plans_button(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Click on the Sidebar menu button
            6. Click on the Subscription plans button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        subscriptions_methods = SubscriptionsPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            main_methods.sidebar_button_click()
            sidebar_methods.click_subscription_plans_button()
            subscription_title = subscriptions_methods.check_for_presence_premium_subscription_title()
            assert isinstance(subscription_title, WebElement)
            qase.create_passed_result(case=119, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=119, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Subscription plans title not found \n {ex}")

    def test_click_faq_support_button(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Click on the Sidebar menu button
            6. Click on the Faq & Support button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        faq_support_methods = FaqSupportPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            main_methods.sidebar_button_click()
            sidebar_methods.click_faq_support_button()
            faq_support_title = faq_support_methods.check_presence_for_faq_support_title()
            assert isinstance(faq_support_title, WebElement)
            qase.create_passed_result(case=15, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=15, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Faq & Support title not found \n {ex}")

    def test_click_about_button(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Click on the Sidebar menu button
            6. Click on the About button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        about_methods = AboutPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            main_methods.sidebar_button_click()
            sidebar_methods.click_about_button()
            about_title = about_methods.check_presence_for_about_title()
            assert isinstance(about_title, WebElement)
            qase.create_passed_result(case=18, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=18, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"About title not found \n {ex}")

    def test_click_back_button(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Click on the Sidebar menu button
            6. Click on the Back button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            main_methods.sidebar_button_click()
            sidebar_methods.click_back_button()
            connect_button = main_methods.check_presence_for_connect_button()
            assert isinstance(connect_button, WebElement)
            qase.create_passed_result(case=252, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=252, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Connect button not found \n {ex}")

    def test_click_sign_in_button(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Click on the Sidebar menu button
            6. Click on the Signin button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            main_methods.sidebar_button_click()
            sidebar_methods.sign_in_button_click()
            sign_in_title = login_methods.check_presence_for_sign_in_title()
            assert isinstance(sign_in_title, WebElement)
            qase.create_passed_result(case=19, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=19, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Sign in title not found \n {ex}")

    def test_click_get_premium_button(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Click on the Sidebar menu button
            6. Click on the Get Premium button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        subscriptions_methods = SubscriptionsPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            main_methods.sidebar_button_click()
            sidebar_methods.get_premium_button_click()
            subscription_title = subscriptions_methods.check_for_presence_subscription_title()
            assert isinstance(subscription_title, WebElement)
            qase.create_passed_result(case=121, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=121, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Subscription title not found \n {ex}")

    def test_click_log_out_button(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Log in as a premium user
            6. Click on the Sidebar menu button
            7. Click on the Log out button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.login_premium_user()
            main_methods.sidebar_button_click()
            sidebar_methods.click_logout_button()
            confirmation_log_out = sidebar_methods.check_presence_for_confirmation_log_out()
            assert isinstance(confirmation_log_out, WebElement)
            qase.create_passed_result(case=120, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=120, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Confirmation log out window not found \n {ex}")

    def test_click_manage_button(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Continue for free" on the advertising window
            5. Log in as a premium user
            6. Click on the Sidebar menu button
            7. Click on the Manage button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        sidebar_methods = SidebarPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.login_premium_user()
            main_methods.sidebar_button_click()
            sidebar_methods.click_manage_button()
            sign_in_title_on_the_site = sidebar_methods.check_presence_for_sign_in_title()
            assert isinstance(sign_in_title_on_the_site, WebElement)
            qase.create_passed_result(case=123, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=123, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Sign in title on the site not found \n {ex}")
































