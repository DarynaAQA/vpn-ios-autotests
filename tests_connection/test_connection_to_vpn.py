from base_classes.appium_methods import AppiumMethods
from base_classes.qase_integration import QASEIntegration
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.advertising_page import AdvertisingPage
from pages.config_adding_page import ConfigAddingPage
from pages.connection_to_vpn_page import ConnectionToVpnPage
from pages.authorization_registration_page import AuthorizationRegistrationPage
from pages.server_select_page import ServerSelectPage
from locators.server_select_locators import PremiumServersLocators, ServerSelectLocators, FreeServersLocators
from dotenv import load_dotenv
from selenium.webdriver.remote.webelement import WebElement
import os
import time


class TestConnection:
    def test_first_connection_to_vpn(self, create_ios_driver_for_real_device, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Allow" to send notifications from app
            5. Click "Continue for free" on the advertising window
            6. Click on Connect button
        """
        appium_methods = AppiumMethods(create_ios_driver_for_real_device)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver_for_real_device)
        advertising_methods = AdvertisingPage(create_ios_driver_for_real_device)
        main_methods = MainPage(create_ios_driver_for_real_device)
        config_adding_methods = ConfigAddingPage(create_ios_driver_for_real_device)
        connection_methods = ConnectionToVpnPage(create_ios_driver_for_real_device)
        qase = QASEIntegration()
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            main_methods.connect_button_click()
            info_window_permission = config_adding_methods.check_presence_for_info_about_permission()
            config_adding_methods.got_it_button_click()
            time.sleep(5)
            connection_methods.check_presence_for_disconnect_button()
            connection_methods.disconnect_button_click()
            assert isinstance(info_window_permission, WebElement)
            qase.create_passed_result(case=106, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=106, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"Information about config installation not found \n {ex}")

    def test_connection_to_free_servers(self, create_ios_driver_for_real_device, qase_run_id, get_start_time):
        """
            STEPS:
            1. Install the app
            2. Launch the app
            3. Click "Agree and Continue" button on the Privacy Policy screen
            4. Click "Allow" to send notifications from app
            5. Click "Continue for free" on the advertising window
            6.
        """
        appium_methods = AppiumMethods(create_ios_driver_for_real_device)
        # privacy_policy_methods = PrivacyPolicyPage(create_ios_driver_for_real_device)
        # advertising_methods = AdvertisingPage(create_ios_driver_for_real_device)
        main_methods = MainPage(create_ios_driver_for_real_device)
        # config_adding_methods = ConfigAddingPage(create_ios_driver_for_real_device)
        connection_methods = ConnectionToVpnPage(create_ios_driver_for_real_device)
        qase = QASEIntegration()
        connection_methods.clear_free_results_file()
        load_dotenv()
        real_ip_address = os.getenv('MY_IP_ADDRESS')
        try:
            # privacy_policy_methods.accept_privacy_policy()
            # advertising_methods.check_presence_for_free_button()
            # time.sleep(2)
            # advertising_methods.continue_for_free_button_click()
            location = appium_methods.is_present('xpath', '//XCUIElementTypeButton[@name="MainChoose'
                                                'ServerButton"]/XCUIElementTypeStaticText[3]').get_attribute('value')
            if location == "Auto":
                try:
                    main_methods.connect_button_click()
                    # config_adding_methods.got_it_button_click()
                    time.sleep(5)
                    connection_methods.check_presence_for_disconnect_button()
                    appium_methods.open_browser()
                    vpn_ip_address = connection_methods.get_current_ip_address()
                    assert vpn_ip_address != real_ip_address
                    with open('results_connection_free_servers.txt', 'a') as file:
                        file.write(f"Auto server - connect is success! {vpn_ip_address} don't match with "
                                   f"{real_ip_address}\n")
                    qase.create_passed_result(case=112, test_run_id=qase_run_id,
                                              time=appium_methods.get_current_time() - get_start_time)
                except Exception as ex:
                    print(f"Error with Auto server connection: {ex}")
            else:
                for server in FreeServersLocators.FreeServers:
                    try:
                        main_methods.select_location_button_click()
                        appium_methods.is_clickable('accessibility_id', f'{server}').click()
                        time.sleep(5)
                        connection_methods.check_presence_for_disconnect_button()
                        appium_methods.close_app(os.getenv("BUNDLE_ID"))
                        appium_methods.open_browser()
                        time.sleep(5)
                        vpn_ip_address = connection_methods.get_current_ip_address()
                        appium_methods.close_browser()
                        appium_methods.activate_app(os.getenv("BUNDLE_ID"))
                        assert vpn_ip_address != real_ip_address
                        main_methods.disconnect_button_click()
                        with open('results_connection_free_servers.txt', 'a') as file:
                            file.write(
                                f"{server} - connect is success! {vpn_ip_address} don't match with {real_ip_address}\n")
                        qase.create_passed_result(case=112, test_run_id=qase_run_id,
                                                  time=appium_methods.get_current_time() - get_start_time)
                    except Exception as ex:
                        print(f"Error with server {server}: {ex}")
        except Exception as ex:
            qase.create_failed_result(case=112, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f" \n {ex}")

    def test_connection_to_premium_servers(self, create_ios_driver_for_real_device, qase_run_id, get_start_time):
        """
            STEPS:
            1. Launch app
            2. Click "Agree and Continue" button on the Privacy Policy screen
            3. Click "Allow" to send notifications from app
            4. Click "Continue for free" on the advertising window
            5. Authorize as a user with a Free subscription
        """
        appium_methods = AppiumMethods(create_ios_driver_for_real_device)
        privacy_policy_methods = PrivacyPolicyPage(create_ios_driver_for_real_device)
        advertising_methods = AdvertisingPage(create_ios_driver_for_real_device)
        main_methods = MainPage(create_ios_driver_for_real_device)
        login_methods = AuthorizationRegistrationPage(create_ios_driver_for_real_device)
        config_adding_methods = ConfigAddingPage(create_ios_driver_for_real_device)
        connection_methods = ConnectionToVpnPage(create_ios_driver_for_real_device)
        server_select_methods = ServerSelectPage(create_ios_driver_for_real_device)
        qase = QASEIntegration()
        load_dotenv()
        real_ip_address = os.getenv('MY_IP_ADDRESS')
        try:
            privacy_policy_methods.accept_privacy_policy()
            advertising_methods.check_presence_for_free_button()
            time.sleep(2)
            advertising_methods.continue_for_free_button_click()
            login_methods.login_premium_user()
            for server in PremiumServersLocators.PremiumServers:
                try:
                    main_methods.select_location_button_click()
                    server_select_methods.server_search_click()
                    appium_methods.is_clickable('class_name', ServerSelectLocators.ServerSearch).send_keys(f'{server}')
                    appium_methods.is_present('accessibility_id', f'{server}').click()
                    # main_methods.connect_button_click()
                    # config_adding_methods.got_it_button_click()
                    time.sleep(5)
                    connection_methods.check_presence_for_disconnect_button()
                    appium_methods.close_app(os.getenv("BUNDLE_ID"))
                    appium_methods.open_browser()
                    vpn_address = connection_methods.get_current_ip_address()
                    appium_methods.close_browser()
                    appium_methods.activate_app(os.getenv("BUNDLE_ID"))
                    main_methods.disconnect_button_click()
                    assert vpn_address != real_ip_address, f"{server}"
                    with open('results_connection_premium_servers.txt', 'a') as file:
                        file.write(f"\n {server} - connect is success! {vpn_address} don't match with {real_ip_address}\n")
                    qase.create_passed_result(case=270, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
                except Exception as ex:
                    print(f"Error with server {server}: {ex}")
                    qase.create_failed_result(case=270, test_run_id=qase_run_id,
                                              time=appium_methods.get_current_time() - get_start_time,
                                              comment=f" \n {ex}")
        except Exception as ex:
            qase.create_failed_result(case=270, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f" \n {ex}")
