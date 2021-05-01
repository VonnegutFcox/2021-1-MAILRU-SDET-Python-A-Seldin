import os
import shutil

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.audiences_page import AudiencesPage
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
# from ui.pages.search_page import SearchPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def dashboard_page(login_page):
    return login_page.login()


@pytest.fixture
def audiences_page(dashboard_page):
    return dashboard_page.go_to_segment()


@pytest.fixture
def campaign_page(dashboard_page):
    return dashboard_page.go_to_campaign()


@pytest.fixture(scope='session')
def base_temp_dir():
    base_dir = '/tmp/tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(base_temp_dir, request):
    test_dir = os.path.join(base_temp_dir, request._pyfuncitem.nodeid)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function')
def driver(config, test_dir):
    url = config['url']
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)