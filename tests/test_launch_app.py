from base_classes.appium_methods import AppiumMethods
from base_classes.qase_integration import QASEIntegration
from pages.launch_page import LaunchPage
from selenium.webdriver.remote.webelement import WebElement


class TestLaunch:
    def test_launch_app(self, create_ios_driver, qase_run_id, get_start_time):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Check for presence of webelements by visually
        """
        appium_methods = AppiumMethods(create_ios_driver)
        launch_methods = LaunchPage(create_ios_driver)
        qase = QASEIntegration()
        try:
            logo = launch_methods.check_presence_for_logo()
            name_app = launch_methods.check_presence_for_name_app()
            launch_loader = launch_methods.check_presence_for_launch_loader()
            assert isinstance(logo, WebElement)
            assert isinstance(name_app, WebElement)
            assert isinstance(launch_loader, WebElement)
            qase.create_passed_result(case=3, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time)
        except Exception as ex:
            qase.create_failed_result(case=3, test_run_id=qase_run_id,
                                      time=appium_methods.get_current_time() - get_start_time,
                                      comment=f"VPN logo not found \n {ex}")
