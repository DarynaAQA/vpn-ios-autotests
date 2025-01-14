from base_classes.appium_methods import AppiumMethods
from base_classes.qase_integration import QASEIntegration
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.authorization_registration_page import AuthorizationRegistrationPage
from pages.sidebar_page import SidebarPage
from pages.advertising_page import AdvertisingPage
from selenium.webdriver.remote.webelement import WebElement
from pages.server_select_page import ServerSelectPage
import time


class TestServerSelect:

    def test_auto_location_free_users(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Allow" to send notifications from app
            5. Click "Continue for free" on the advertising window
        """
        appium_methods = AppiumMethods(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            name_location = main_methods.get_name_current_location()
            assert name_location == "Auto"
            qase.create_passed_result(case=164, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=164, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Auto location not found \n {ex}")

    def test_available_premium_servers(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Launch app
            2. Click "Agree and Continue" button on the Privacy Policy screen
            3. Click "Allow" to send notifications from app
            4. Click "Continue for free" on the advertising window
            5. Log in a premium user
            6. Click on Select server button
        """
        appium_methods = AppiumMethods(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        server_select_methods = ServerSelectPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.login_premium_user()
            main_methods.select_location_button_click()
            albania_server = server_select_methods.check_for_presence_albania_server()
            finland_server = server_select_methods.check_presence_for_finland_server()
            new_york_server = server_select_methods.check_presence_for_new_york_server()
            assert isinstance(albania_server, WebElement), f"{albania_server}"
            assert isinstance(finland_server, WebElement), f"{finland_server}"
            assert isinstance(new_york_server, WebElement), f"{new_york_server}"
            qase.create_passed_result(case=101, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=101, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Premium server not found \n {ex}")

    def test_favorites_servers(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Launch app
            2. Click "Agree and Continue" button on the Privacy Policy screen
            3. Click "Allow" to send notifications from app
            4. Click "Continue for free" on the advertising window
            5. Login as a premium user
            6. Click on select server button
            7. Added first premium server
            8. Click on favorites servers
        """
        appium_methods = AppiumMethods(create_ios_driver)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver)
        advertising_methods = AdvertisingPage(create_ios_driver)
        main_methods = MainPage(create_ios_driver)
        server_select_methods = ServerSelectPage(create_ios_driver)
        login_methods = AuthorizationRegistrationPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.login_premium_user()
            main_methods.select_location_button_click()
            server_select_methods.add_server_to_favorites()
            server_select_methods.favorites_servers_click()
            albania_server = server_select_methods.check_for_presence_albania_server()
            assert isinstance(albania_server, WebElement)
            qase.create_passed_result(case=103, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=103, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Albania server not found \n {ex}")







