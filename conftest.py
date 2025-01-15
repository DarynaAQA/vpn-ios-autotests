import datetime
from base_classes.qase_integration import QASEIntegration
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
import pytest
import requests
from dotenv import load_dotenv, set_key
import subprocess
from subprocess import Popen
import time


APPIUM_PORT = 4723
APPIUM_HOST = '0.0.0.0'

# @pytest.fixture(scope="session")
# def appium_server():
#     # Запуск Appium сервера
#     print("Starting Appium server...")
#     server_process = Popen(["appium"])  # или команда для запуска сервера на вашем окружении
#     time.sleep(5)  # Ожидание для запуска сервера
#
#     yield server_process
#
#     # Остановка Appium сервера
#     print("Stopping Appium server...")
#     server_process.terminate()
#


@pytest.fixture(scope='function')
def create_ios_driver(app_path):
    options = XCUITestOptions()
    options.platform_name = 'iOS'
    options.platform_version = '17.5'
    options.device_name = 'iPhone 15'
    options.udid = 'CCFBAE69-DB3D-4387-8632-7937449C322A'
    options.automation_name = 'XCUITest'
    options.app = app_path
    options.auto_accept_alerts = True
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def create_ios_driver_for_real_device(app_path):
    options = XCUITestOptions()
    options.platform_name = 'iOS'
    options.platform_version = '17.4.1'
    options.device_name = 'iPhone 14 Pro'
    options.udid = '00008120-001431CE0E58201E'
    options.automation_name = 'XCUITest'
    options.app = app_path
    options.auto_dismiss_alerts = True
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', options=options)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--name", action="store", default="vpn", help="Choose name app for VPN"
    )

    parser.addoption(
        "--device", action="store", default="s", help="Choose type of device"
    )


@pytest.fixture(scope="session", autouse=True)
def app_path(request):
    name_app = request.config.getoption("--name")
    device = request.config.getoption("--device")

    if name_app == "name_app" and device == "s":
        APP_PATH = "app_path"

        BUNDLE_ID = "bundle_id"
        load_dotenv()
        env_path = '.env'
        set_key(env_path, 'BUNDLE_ID', BUNDLE_ID)

    elif name_app == "name_app" and device == "r":
        APP_PATH = "app_path"

        BUNDLE_ID = "bundle_id"
        load_dotenv()
        env_path = '.env'
        set_key(env_path, 'BUNDLE_ID', BUNDLE_ID)

    elif name_app == "name_app" and device == "s":
        APP_PATH = "app_path"

        BUNDLE_ID = "bundle_id"
        load_dotenv()
        env_path = '.env'
        set_key(env_path, 'BUNDLE_ID', BUNDLE_ID)

    elif name_app == "name_app" and device == "r":
        APP_PATH = "app_path"

        BUNDLE_ID = "bundle_id"
        load_dotenv()
        env_path = '.env'
        set_key(env_path, 'BUNDLE_ID', BUNDLE_ID)

    elif name_app == "name_app" and device == "s":
        APP_PATH = "app_path"

        BUNDLE_ID = "bundle_id"
        load_dotenv()
        env_path = '.env'
        set_key(env_path, 'BUNDLE_ID', BUNDLE_ID)

    elif name_app == "name_app" and device == "r":
        APP_PATH = "app_path"

        BUNDLE_ID = "bundle_id"
        load_dotenv()
        env_path = '.env'
        set_key(env_path, 'BUNDLE_ID', BUNDLE_ID)

    elif name_app == "name_app" and device == "s":
        APP_PATH = "app_path"

        BUNDLE_ID = "bundle_id"
        load_dotenv()
        env_path = '.env'
        set_key(env_path, 'BUNDLE_ID', BUNDLE_ID)

    elif name_app == "name_app" and device == "r":
        APP_PATH = "app_path"

        BUNDLE_ID = "bundle_id"
        load_dotenv()
        env_path = '.env'
        set_key(env_path, 'BUNDLE_ID', BUNDLE_ID)

    else:
        raise ValueError(f"Unsupported version app: {name_app}")

    return APP_PATH


# @pytest.fixture(scope='session')
# def appium_service():
#     service = AppiumService()
#     service.start(
#         args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
#         timeout_ms=20000,
#     )
#     print("Appium service started: ", service.is_running)
#     print("Appium service is listening: ", service.is_listening)
#     yield service
#     service.stop()


@pytest.fixture(scope='session', autouse=True)
def qase_run_id():
    """
        The fixture create new test run id, which depends on specific test plan id. Returns id of created test run.
    """
    qase_run = QASEIntegration()
    test_run = qase_run.create_test_run(test_plan_id=4)
    return test_run


@pytest.fixture(scope='function')
def get_start_time():
    start_time = datetime.datetime.now()
    time_part = str(start_time).split()[1]
    time_without_ms = time_part.split('.')[0]
    hours, minutes, seconds = map(int, time_without_ms.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    yield total_seconds


@pytest.fixture(scope='session', autouse=False)
def send_test_run(qase_run_id):
    qase_run = QASEIntegration()
    start_hours = datetime.datetime.now()
    yield
    url = qase_run.update_publicity_test_run(qase_run_id)
    end_hours = datetime.datetime.now()
    result = end_hours - start_hours
    trimmed_time = str(result).split('.')[0]
    qase_run.send_test_run_url_to_slack(url, test_time=trimmed_time)


@pytest.fixture(scope='session', autouse=True)
def save_ip_to_env():
    response = requests.get('https://api.ipify.org?format=json')
    ip_address = response.json()['ip']
    response = requests.get('https://ipinfo.io')
    country_code = response.json()['country']

    load_dotenv()
    env_path = '.env'
    set_key(env_path, 'MY_IP_ADDRESS', ip_address)
    set_key(env_path, 'MY_COUNTRY_CODE', country_code)


@pytest.fixture(scope='session', autouse=False)
def cleanup_after_all_tests(request):
    """
        Fixture to clean up environment variables after all tests are executed
    """
    def finalizer():
        load_dotenv()
        clear_env()

    request.addfinalizer(finalizer)


def clear_env() -> None:
    load_dotenv()
    env_path = '.env'
    set_key(env_path, 'MY_IP_ADDRESS', '')
    set_key(env_path, 'MY_COUNTRY_CODE', '')
    set_key(env_path, 'BUNDLE_ID', '')





