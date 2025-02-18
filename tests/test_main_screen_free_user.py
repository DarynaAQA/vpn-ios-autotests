from base_classes.appium_methods import AppiumMethods
from base_classes.qase_integration import QASEIntegration
from pages.main_page import MainPage
from selenium.webdriver.remote.webelement import WebElement
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.advertising_page import AdvertisingPage
import time


class TestMainScreenFreeUser:

    def test_presence_elements_main_screen_free_user(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Launch app
            2. Click "Agree and Continue" button on the Privacy Policy screen
            3. Click "Allow" to send notifications from app
            4. Click "Continue for free" on the advertising window
            5. Check for presence elements on the main screen for free user
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
            sidebar_button = main_methods.check_presence_for_sidebar_button()
            app_name = main_methods.check_presence_for_app_name()
            account_button = main_methods.check_presence_for_account_button()
            select_location_button = main_methods.check_presence_for_select_location_button()
            your_location = main_methods.check_presence_for_your_location()
            protect_icon = main_methods.check_presence_for_protect_icon()
            protect_status = main_methods.check_presence_for_protect_status()
            connect_button = main_methods.check_presence_for_connect_button()
            remove_ads_button = main_methods.check_presence_for_remove_ads_button()
            ads_banner = main_methods.check_presence_for_ads_banner()
            assert isinstance(sidebar_button, WebElement)
            assert isinstance(app_name, WebElement)
            assert isinstance(account_button, WebElement)
            assert isinstance(select_location_button, WebElement)
            assert isinstance(your_location, WebElement)
            assert isinstance(protect_icon, WebElement)
            assert isinstance(protect_status, WebElement)
            assert isinstance(connect_button, WebElement)
            assert isinstance(remove_ads_button, WebElement)
            assert isinstance(ads_banner, WebElement)
            qase.create_passed_result(case=4, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=4, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"No elements found \n {ex}")

